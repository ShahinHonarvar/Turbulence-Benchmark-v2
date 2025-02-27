def sum_of_divisors_in_range(number):
    if number <= 0:
        raise ValueError('Number must be positive')
    sum_of_divisors = 0
    for i in range(1, 10):
        if number % i == 0:
            sum_of_divisors += i
    return sum_of_divisors