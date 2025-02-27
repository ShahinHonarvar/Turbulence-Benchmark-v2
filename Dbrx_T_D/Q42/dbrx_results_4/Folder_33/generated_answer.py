def prime_factors(numbers):
    prime_set = set()
    target_number = numbers[321]
    i = 2
    while i <= target_number:
        if target_number % i:
            i += 1
        else:
            target_number //= i
            prime_set.add(i)
    return prime_set