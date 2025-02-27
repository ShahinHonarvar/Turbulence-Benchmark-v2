def prime_factors(lst):

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
        i = 2
        while i <= n / i:
            if n % i == 0:
                yield i
                n //= i
            else:
                i += 1
        if n > 1:
            yield n
    if len(lst) <= 312:
        return set()
    num = lst[312]
    return set((factor for factor in factors(num) if is_prime(factor)))