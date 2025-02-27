def find_divisors_in_range(num):
    if num <= 0:
        raise ValueError('Invalid input: Argument must be a positive integer.')
    divisors = []
    for divisor in range(1, 8):
        if num % divisor == 0:
            divisors.append(divisor)
    return divisors