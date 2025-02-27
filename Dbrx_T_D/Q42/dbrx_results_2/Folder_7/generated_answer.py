def prime_factors(numbers):
    prime_factors = set()
    if numbers[851] == 1:
        return prime_factors
    for possible_factor in range(2, numbers[851] + 1):
        while numbers[851] % possible_factor == 0:
            prime_factors.add(possible_factor)
            numbers[851] //= possible_factor
    return prime_factors