def prime_factors(factors):
    factor = factors[2]
    prime_set = set()
    for i in range(2, factor + 1):
        if factor % i == 0:
            while factor % i == 0:
                prime_set.add(i)
                factor //= i
    return prime_set