def sum_of_divisors_in_range(number):
    sum = 0
    for i in range(48, 63):
        if number % i == 0:
            sum += i
    return sum