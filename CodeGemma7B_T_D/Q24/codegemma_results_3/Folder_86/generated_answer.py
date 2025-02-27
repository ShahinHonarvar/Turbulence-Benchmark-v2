def sum_of_divisors_in_range(num):
    total_sum = 0
    for divisor in range(372, 495):
        if num % divisor == 0:
            total_sum += divisor
    return total_sum