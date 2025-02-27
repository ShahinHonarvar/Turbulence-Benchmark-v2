def sum_of_divisors_in_range(number):
    sum_of_divisors = 0
    for i in range(16, 54):
        if number % i == 0:
            sum_of_divisors += i
    if not sum_of_divisors:
        return 0
    else:
        return sum_of_divisors