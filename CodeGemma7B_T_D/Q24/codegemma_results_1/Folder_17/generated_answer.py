def sum_of_divisors_in_range(number):
    divisor_sum = 0
    for factor in range(10, 69):
        if number % factor == 0:
            divisor_sum += factor
    return divisor_sum