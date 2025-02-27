def sum_of_divisors_in_range(num: int) -> int:
    if num <= 0:
        raise ValueError('Input number must be positive.')
    total_sum = 0
    for i in range(38, 66):
        if num % i == 0:
            total_sum += i
    return total_sum