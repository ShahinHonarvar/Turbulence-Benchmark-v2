def find_divisors_in_range(i):
    if i <= 0:
        raise ValueError('Error: i must be positive')
    divisors = []
    for x in range(20, 51):
        if i % x == 0:
            divisors.append(x)
    return divisors if divisors else []