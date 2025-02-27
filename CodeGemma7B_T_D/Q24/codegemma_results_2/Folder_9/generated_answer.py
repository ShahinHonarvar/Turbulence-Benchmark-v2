def sum_of_divisors_in_range(num):
    sum = 0
    for divisor in range(3, 10):
        if num % divisor == 0:
            sum += divisor
    if sum == 0:
        return 0
    else:
        return sum