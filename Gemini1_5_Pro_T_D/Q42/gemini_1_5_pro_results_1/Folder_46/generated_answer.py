def prime_factors(numbers):
    target_number = numbers[453]
    prime_factors_set = set()
    i = 2
    while i * i <= target_number:
        if target_number % i == 0:
            prime_factors_set.add(i)
            target_number //= i
        else:
            i += 1
    if target_number > 1:
        prime_factors_set.add(target_number)
    return prime_factors_set