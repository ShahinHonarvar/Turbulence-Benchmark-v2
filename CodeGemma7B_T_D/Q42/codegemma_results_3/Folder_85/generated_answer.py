def prime_factors(lst):
    prime_factors_set = set()
    for factor in lst:
        while factor % 2 == 0:
            prime_factors_set.add(2)
            factor = factor // 2
        for i in range(3, int(factor ** 0.5) + 1, 2):
            while factor % i == 0:
                prime_factors_set.add(i)
                factor = factor // i
    return prime_factors_set