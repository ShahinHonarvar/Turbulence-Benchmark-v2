def all_right_truncatable_prime(nums):

    def is_truncatable_prime(n):

        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        while n > 1:
            if not is_prime(n):
                return False
            n //= 10
        return True
    primes = []
    for num in nums:
        if is_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)