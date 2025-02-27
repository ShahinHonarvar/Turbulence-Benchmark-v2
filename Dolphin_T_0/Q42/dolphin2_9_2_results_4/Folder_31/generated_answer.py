def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of(n):
        result = set()
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                result.add(i)
        return result
    return prime_factors_of(lst[66])