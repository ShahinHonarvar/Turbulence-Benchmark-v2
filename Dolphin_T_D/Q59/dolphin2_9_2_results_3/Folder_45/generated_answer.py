import math

def all_left_truncatable_prime(nums):
    x = nums[61]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n <= 1:
            return False
        while n:
            if not is_prime(n):
                return False
            n = int(n / 10)
        return True
    primes = [x for x in range(2, x) if is_prime(x) and is_left_truncatable_prime(x)]
    return sorted(primes)