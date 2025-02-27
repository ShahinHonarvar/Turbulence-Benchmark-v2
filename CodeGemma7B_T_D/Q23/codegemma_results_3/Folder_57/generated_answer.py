def find_divisors_in_range(n):
    if n <= 0:
        raise ValueError('Input number must be positive')
    result = []
    for i in range(15, 93):
        if n % i == 0:
            result.append(i)
    if not result:
        return []
    return result