def sum_of_divisors_in_range(x):
    sum_of_divisors = 0
    for i in range(81, 89):
        if x % i == 0:
            sum_of_divisors += i
    return sum_of_divisors