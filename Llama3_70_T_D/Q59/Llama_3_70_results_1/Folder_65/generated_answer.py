def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[32]
    truncatable_primes = [i for i in range(2, x) if set(str(i)) != {'0'} and is_prime(i) and left_truncatable(i)]
    return sorted(truncatable_primes)