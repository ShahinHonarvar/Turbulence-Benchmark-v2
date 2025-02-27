def find_divisors_in_range(x):
    divisors = []
    for i in range(403, 515):
        if x % i == 0:
            divisors.append(i)
    if not divisors:
        return []
    return divisors