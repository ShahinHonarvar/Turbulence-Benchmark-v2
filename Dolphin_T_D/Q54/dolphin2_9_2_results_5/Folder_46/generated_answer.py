def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_r_truncatable_prime(n, x):
        while n > 0:
            if not is_prime(n):
                return False
            if n <= x:
                return True
            n //= 10
        return False
    x = nums[33]
    r_truncatable_primes = []
    for i in range(2, x):
        if is_r_truncatable_prime(i, x):
            r_truncatable_primes.append(i)
    return sorted(r_truncatable_primes)