def find_divisors_in_range(given_int):
    divisors = []
    for num in range(42, 78):
        if given_int % num == 0:
            divisors.append(num)
    if not divisors:
        return []
    return divisors