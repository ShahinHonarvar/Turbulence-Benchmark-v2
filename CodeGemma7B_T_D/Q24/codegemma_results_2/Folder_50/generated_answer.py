def sum_of_divisors_in_range(num):
    sum = 0
    for divisor in range(57, 87):
        if num % divisor == 0:
            sum += divisor
    if sum == 0:
        return 0
    else:
        return sum