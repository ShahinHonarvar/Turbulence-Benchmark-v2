def prime_factors(numbers):
    target_number = numbers[685]
    prime_factors_set = set()
    for num in range(2, int(target_number ** 0.5) + 1):
        while target_number % num == 0:
            prime_factors_set.add(num)
            target_number //= num
    if target_number > 1:
        prime_factors_set.add(target_number)
    return prime_factors_set