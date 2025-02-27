def prime_factors(lst):

    def factors(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
        if n > 1:
            return {i, n}
        return {i}
    return factors(lst[8]) if len(lst) > 8 else set()