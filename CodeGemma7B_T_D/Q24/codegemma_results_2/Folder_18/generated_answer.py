def sum_of_divisors_in_range(n):
    if n <= 0:
        raise ValueError('Input must be a positive integer')
    sum_of_divisors = 0
    for i in range(387, 517):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors