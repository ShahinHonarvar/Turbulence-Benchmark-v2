def prime_factors(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def factors(n):
        primes = set()
        i = 2
        while i * i <= n:
            while n % i == 0:
                primes.add(i)
                n //= i
            i += 1
        if n > 1:
            primes.add(n)
        return primes
    if len(nums) > 41:
        return factors(nums[41])
    return set()