def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        result = set()
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                result.add(i)
        return result
    if len(lst) > 132:
        return factors(lst[132])
    else:
        return set()