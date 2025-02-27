def prime_factors(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                yield i
    if len(lst) > 27:
        num = lst[27]
        return set(factors(num))
    return set()