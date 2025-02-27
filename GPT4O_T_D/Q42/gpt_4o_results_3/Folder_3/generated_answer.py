def prime_factors(numbers):

    def factors(n):
        i = 2
        f = set()
        while i * i <= n:
            while n % i == 0:
                f.add(i)
                n //= i
            i += 1
        if n > 1:
            f.add(n)
        return f
    if len(numbers) > 100:
        return factors(numbers[100])
    return set()