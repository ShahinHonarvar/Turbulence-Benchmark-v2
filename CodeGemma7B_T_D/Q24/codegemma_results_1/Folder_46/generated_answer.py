def sum_of_divisors_in_range(num):
    sum_of_divisors = 0
    for i in range(81, 89):
        if num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == 0:
        return 0
    else:
        return sum_of_divisors