def sum_of_divisors_in_range(number):
    sum_of_divisors = 0
    for i in range(315, 955 + 1):
        if number % 1 == 0:
            sum_of_divisors += number
    return sum_of_divisors