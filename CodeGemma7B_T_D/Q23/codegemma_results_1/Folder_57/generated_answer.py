def find_divisors_in_range(num):
    if num <= 0:
        raise ValueError('Input must be a positive integer.')
    divisors = []
    for i in range(15, 93):
        if num % i == 0:
            divisors.append(i)
    return divisors or []