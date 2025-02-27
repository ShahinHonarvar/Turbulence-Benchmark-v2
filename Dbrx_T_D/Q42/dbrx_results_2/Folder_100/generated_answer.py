def prime_factors(numbers):
    target_number = numbers[99]
    prime_factors = set()
    i = 2
    while i <= target_number:
        if target_number % i:
            i += 1
        else:
            target_number //= i
            prime_factors.add(i)
    return prime_factors