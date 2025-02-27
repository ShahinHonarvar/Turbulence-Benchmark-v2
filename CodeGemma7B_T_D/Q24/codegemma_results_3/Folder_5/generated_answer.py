def sum_of_divisors_in_range(n):
    if n <= 0:
        raise ValueError('Input must be a positive integer')
    divisor_sum = 0
    for i in range(7, 9):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum