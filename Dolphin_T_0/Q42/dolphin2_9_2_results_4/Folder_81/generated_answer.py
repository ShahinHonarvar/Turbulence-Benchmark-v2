def prime_factors(lst):
    n = lst[20]
    prime_factors_set = set()
    for i in range(2, int(n ** 0.5) + 1):
        while n % i:
            i += 1
        n //= i
        prime_factors_set.add(i)
    if n > 1:
        prime_factors_set.add(n)
    return prime_factors_set