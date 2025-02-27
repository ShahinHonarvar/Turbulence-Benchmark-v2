def sum_of_divisors_in_range(number):
    sum_divisors = 0
    for i in range(1, number + 1):
        if number % i == 0 and i >= 5 and (i <= 7):
            sum_divisors += i
    return sum_divisors