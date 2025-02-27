def sum_of_divisors_in_range(num: int) -> int:
    if num <= 0:
        raise ValueError('Input number must be positive.')
    divisors_sum = 0
    for divisor in range(2, 8):
        if num % divisor == 0:
            divisors_sum += divisor
    return divisors_sum