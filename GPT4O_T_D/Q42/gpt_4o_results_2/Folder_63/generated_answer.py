def prime_factors(numbers):
    if len(numbers) <= 57:
        return set()
    n = numbers[57]
    i = 2
    prime_factors_set = set()
    while i * i <= n:
        while n % i == 0:
            prime_factors_set.add(i)
            n //= i
        i += 1
    if n > 1:
        prime_factors_set.add(n)
    return prime_factors_set