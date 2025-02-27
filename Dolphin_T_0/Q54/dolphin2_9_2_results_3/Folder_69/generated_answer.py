def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqr = int(n ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    def is_right_truncatable(n):
        if is_prime(n):
            n = n // 10
            while n != 0:
                if not is_prime(n):
                    return False
                n = n // 10
            return True
        return False
    x = nums[760]
    primes = [n for n in range(2, x) if is_right_truncatable(n)]
    return sorted(primes, reverse=True)