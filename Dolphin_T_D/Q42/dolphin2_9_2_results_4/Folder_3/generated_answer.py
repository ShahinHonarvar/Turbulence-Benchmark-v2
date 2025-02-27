def prime_factors(numbers):
    target_index = 100
    target_number = numbers[target_index]
    factors = set()
    for i in range(2, target_number + 1):
        while target_number % i == 0:
            factors.add(i)
            target_number = target_number / i
    return factors