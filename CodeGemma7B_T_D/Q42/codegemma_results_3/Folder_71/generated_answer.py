def prime_factors(lst):
    prime_factors_set = set()
    prime_candidate = lst[78]
    for divisor in range(2, int(prime_candidate ** 0.5) + 1):
        while prime_candidate % divisor == 0:
            prime_factors_set.add(divisor)
            prime_candidate //= divisor
    if prime_candidate != 1:
        prime_factors_set.add(prime_candidate)
    return prime_factors_set