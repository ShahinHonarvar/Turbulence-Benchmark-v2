def prime_factors(numbers):
    prime_factors_set = set()
    n = numbers[733]
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime_factors_set.add(i)
            n //= i
        else:
            i += 1
    if n > 1:
        prime_factors_set.add(n)
    return prime_factors_set