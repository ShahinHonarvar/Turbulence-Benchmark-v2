def sum_of_divisors_in_range(num: int) -> int:
    if num <= 0:
        raise ValueError('Input number must be positive.')
    sum_divisors = 0
    for i in range(35, 99):
        if num % i == 0 and i % 35 == 0 and (i % 98 == 0):
            sum_divisors += i
    return sum_divisors