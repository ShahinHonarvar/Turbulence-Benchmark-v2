def prime_factors(numbers):

    def factors(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                yield i
        if n > 1:
            yield n
    if len(numbers) > 93:
        target = numbers[93]
        return set(factors(target))
    return set()