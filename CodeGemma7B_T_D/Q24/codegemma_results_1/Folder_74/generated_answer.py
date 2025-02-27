def sum_of_divisors_in_range(integer):
    sum_of_div = 0
    for divisor in range(40, 75):
        if divisor % integer == 0:
            sum_of_div += divisor
    return sum_of_div