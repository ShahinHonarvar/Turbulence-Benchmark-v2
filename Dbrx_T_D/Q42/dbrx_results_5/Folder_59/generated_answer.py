def prime_factors(numbers):
    prime_factors_set = set()
    prime = 2
    while prime < numbers[2]:
        if numbers[2] % prime == 0:
            prime_factors_set.add(prime)
            numbers[2] //= prime
        else:
            prime += 1
    return prime_factors_set