def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[86]
    right_trunc_primes = []
    for num in range(x - 1, 1, -1):
        str_num = str(num)
        is_right_trunc = True
        for i in range(len(str_num)):
            trunc_num = int(str_num[:len(str_num) - i])
            if not is_prime(trunc_num):
                is_right_trunc = False
                break
        if is_right_trunc and is_prime(num):
            right_trunc_primes.append(num)
    return sorted(right_trunc_primes, reverse=True)