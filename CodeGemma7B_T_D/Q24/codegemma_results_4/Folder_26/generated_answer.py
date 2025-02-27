def sum_of_divisors_in_range(number):
    divisors = [i for i in range(2, number + 1) if number % i == 0]
    sum = 0
    for divisor in divisors:
        if divisor >= 83 and divisor <= 95:
            sum += divisor
    return sum