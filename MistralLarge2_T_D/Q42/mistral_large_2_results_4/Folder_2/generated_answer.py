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
        factors_set = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if is_prime(i):
                    factors_set.add(i)
                if is_prime(n // i):
                    factors_set.add(n // i)
        if is_prime(n):
            factors_set.add(n)
        return factors_set
    if len(nums) > 702:
        return factors(nums[702])
    return set()