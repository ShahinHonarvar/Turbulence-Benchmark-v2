def sum_of_divisors_in_range(number):
    total_sum = 0
    for divisor in range(403, 515):
        if number % divisor == 0:
            total_sum += divisor
    return total_sum if total_sum != 0 else 0