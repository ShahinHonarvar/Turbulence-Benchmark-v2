def sum_of_divisors_in_range(num: int) -> int:
    if num <= 0:
        raise ValueError('Input must be a positive integer.')
    sum_divisors = 0
    for i in range(50, 85):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors