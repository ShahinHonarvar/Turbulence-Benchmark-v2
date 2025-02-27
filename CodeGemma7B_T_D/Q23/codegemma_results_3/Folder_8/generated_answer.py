def find_divisors_in_range(number):
    if number <= 0:
        raise ValueError('Number must be positive')
    divisors = []
    for i in range(48, 63):
        if number % i == 0:
            divisors.append(i)
    return divisors or []