def sum_of_divisors_in_range(n):
    total = 0
    for divisor in range(372, 495):
        if n % divisor == 0:
            total += divisor
    return total