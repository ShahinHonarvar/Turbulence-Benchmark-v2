def sum_of_divisors_in_range(num: int) -> int:
    if num <= 0:
        raise ValueError('Input number must be positive.')
    divisor_sum = 0
    for i in range(46, 66):
        if num % i == 0:
            divisor_sum += i
    return divisor_sum