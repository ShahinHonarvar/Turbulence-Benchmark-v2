def prime_factors(numbers):
    target_number = numbers[72]
    prime_factors_set = set()
    for i in range(2, int(target_number ** 0.5) + 1):
        while target_number % i == 0:
            prime_factors_set.add(i)
            target_number //= i
    if target_number > 1:
        prime_factors_set.add(target_number)
    return prime_factors_set