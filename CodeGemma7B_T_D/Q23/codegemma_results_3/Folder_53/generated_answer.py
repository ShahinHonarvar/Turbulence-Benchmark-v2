def find_divisors_in_range(num):
    if num <= 0:
        raise ValueError('Number must be positive')
    divisors = []
    for i in range(4, 10):
        if num % i == 0:
            divisors.append(i)
    return divisors