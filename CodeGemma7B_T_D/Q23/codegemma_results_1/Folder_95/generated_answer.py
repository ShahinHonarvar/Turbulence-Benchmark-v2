def find_divisors_in_range(num):
    if num < 0:
        raise ValueError('Input number must be positive.')
    divisors = []
    for i in range(35, 99):
        if num % i == 0:
            divisors.append(i)
    if not divisors:
        return []
    return divisors