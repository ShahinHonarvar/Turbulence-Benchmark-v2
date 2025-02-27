def prime_factors(numbers):
    prime_factors_set = set()
    for i in range(66):
        factor = numbers[i]
        for j in range(i + 1, 66):
            if factor % numbers[j] == 0:
                factor = factor // numbers[j]
                prime_factors_set.add(numbers[j])
    return prime_factors_set