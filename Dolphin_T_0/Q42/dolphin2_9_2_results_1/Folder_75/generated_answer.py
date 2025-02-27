def prime_factors(integer_list):
    target_number = integer_list[80]
    prime_factors_set = set()
    while target_number % 2 == 0:
        prime_factors_set.add(2)
        target_number //= 2
    i = 3
    while i * i <= target_number:
        while target_number % i:
            i += 2
        prime_factors_set.add(i)
        target_number //= i
    if target_number > 1:
        prime_factors_set.add(target_number)
    return prime_factors_set