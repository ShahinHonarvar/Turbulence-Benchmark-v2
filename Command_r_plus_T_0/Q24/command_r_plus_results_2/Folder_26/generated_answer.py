def sum_of_divisors_in_range(num: int) -> int:
    if num <= 0:
        raise ValueError('Input number must be positive.')
    sum_divisors = 0
    for divisor in range(83, 96):
        if num % divisor == 0:
            sum_divisors += divisor
    return sum_divisors