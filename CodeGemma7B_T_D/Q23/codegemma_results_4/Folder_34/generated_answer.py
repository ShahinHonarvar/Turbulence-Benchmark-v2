def find_divisors_in_range(num):
    if num <= 0:
        raise ValueError('Input must be a positive number')
    divisors = []
    for i in range(4, 6):
        if num % i == 0:
            divisors.append(i)
    return divisors or []