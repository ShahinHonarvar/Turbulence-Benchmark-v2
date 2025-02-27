def sum_of_divisors_in_range(num):
    divisor = 5
    sum = 0
    while divisor <= num:
        if num % divisor == 0 and divisor <= 7:
            sum += divisor
        divisor += 1
    if sum == 0:
        return 0
    else:
        return sum