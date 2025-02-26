def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[71]
    left_trunc_primes = []
    for num in range(x - 1, 1, -1):
        if '0' not in str(num):
            is_left_trunc = True
            str_num = str(num)
            while len(str_num) > 1:
                str_num = str_num[1:]
                if not is_prime(int(str_num)):
                    is_left_trunc = False
                    break
            if is_left_trunc and is_prime(num):
                left_trunc_primes.append(num)
    return sorted(left_trunc_primes, reverse=True)