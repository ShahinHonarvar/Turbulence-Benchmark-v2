def prime_factors(lst):

    def factors(n):
        i = 2
        result = set()
        while i * i <= n:
            while n % i == 0:
                result.add(i)
                n //= i
            i += 1
        if n > 1:
            result.add(n)
        return result
    if 459 < len(lst):
        return factors(lst[459])
    else:
        return set()