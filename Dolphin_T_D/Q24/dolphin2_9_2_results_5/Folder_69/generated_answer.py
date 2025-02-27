def sum_of_divisors_in_range(positive_integer):
    sum_of_divisors = 0
    for divisor in range(658, 869):
        if positive_integer % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors