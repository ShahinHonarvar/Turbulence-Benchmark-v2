def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[945]
    right_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        is_right_truncatable_prime = True
        for i in range(len(str_num)):
            trunc_num = int(str_num[:-i or len(str_num)])
            if not is_prime(trunc_num):
                is_right_truncatable_prime = False
                break
        if is_right_truncatable_prime:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)