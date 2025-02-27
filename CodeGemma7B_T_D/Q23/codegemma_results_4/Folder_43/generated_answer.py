def find_divisors_in_range(num):
    if not isinstance(num, int):
        raise TypeError('The input argument must be an integer.')
    if num <= 0:
        raise ValueError('The input argument must be positive.')
    divisors = []
    for i in range(19, 70):
        if num % i == 0:
            divisors.append(i)
    return divisors