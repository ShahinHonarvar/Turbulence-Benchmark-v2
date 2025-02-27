def sum_of_divisors_in_range(num):
    if num <= 0:
        return 0
    sum_of_divisors = 0
    for i in range(59, 89):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors