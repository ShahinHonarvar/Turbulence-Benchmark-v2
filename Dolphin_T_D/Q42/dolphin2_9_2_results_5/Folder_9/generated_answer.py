def prime_factors(george):
    prime_factors_set = set()
    num = george[24]
    for i in range(2, num + 1):
        while num % i == 0:
            prime_factors_set.add(i)
            num = num / i
    return prime_factors_set