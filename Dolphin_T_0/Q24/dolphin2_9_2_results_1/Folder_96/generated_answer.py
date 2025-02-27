def sum_of_divisors_in_range(num):
    if num < 0:
        raise ValueError('Input must be a positive integer.')
    result = 0
    for i in range(5, 10):
        if num % i == 0:
            result += i
    return result