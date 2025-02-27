def sum_of_divisors_in_range(num: int) -> int:
    if num <= 0:
        raise ValueError('Input number must be positive.')
    divisors_sum = 0
    for i in range(4, 7):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum