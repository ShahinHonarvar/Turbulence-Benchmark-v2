def all_left_right_truncatable_prime(nums):
    x = nums[70]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            s_num = str(num)
            is_truncatable = True
            while len(s_num) > 1:
                if not is_prime(int(s_num)) or '0' in s_num:
                    is_truncatable = False
                    break
                s_num = s_num[1:]
                s_num = s_num[:-1]
            if is_truncatable:
                primes.append(num)
    primes.sort(reverse=True)
    return primes

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True