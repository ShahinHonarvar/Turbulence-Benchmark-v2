def sum_of_divisors_in_range(positive_integer):
    sum_of_divisors = 0
    for i in range(42, 78):
        if positive_integer % i == 0:
            sum_of_divisors = sum_of_divisors + i
    return sum_of_divisors