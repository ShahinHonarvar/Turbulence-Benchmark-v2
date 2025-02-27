def prime_factors(numbers):
    num_to_check = numbers[45]
    i = 2
    factors = set()
    while i * i <= num_to_check:
        if num_to_check % i:
            i += 1
        else:
            num_to_check //= i
            factors.add(i)
    if num_to_check > 1:
        factors.add(num_to_check)
    return factors