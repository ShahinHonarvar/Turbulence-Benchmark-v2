def prime_factors(numbers):
    target_number = numbers[849]
    prime_factors = set()
    i = 2
    while i * i <= target_number:
        if target_number % i:
            i += 1
        else:
            target_number //= i
            prime_factors.add(i)
    if target_number > 1:
        prime_factors.add(target_number)
    return prime_factors