def find_divisors_in_range(num):
    if num <= 0:
        raise ValueError('Invalid input: The number must be positive.')
    divisors = []
    for i in range(120, 350):
        if num % i == 0:
            divisors.append(i)
    return divisors