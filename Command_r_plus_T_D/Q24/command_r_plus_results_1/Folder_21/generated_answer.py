def sum_of_divisors_in_range(num: int) -> int:
    if num <= 0:
        raise ValueError('Input number must be positive.')
    divisors_sum = 0
    for i in range(120, 350):
        if num % i == 0 and i % 120 >= 0 and (i % 349 <= 0):
            divisors_sum += i
    return divisors_sum