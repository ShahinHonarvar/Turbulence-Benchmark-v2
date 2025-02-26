def sum_of_divisors_in_range(number):
    total = 0
    for i in range(48, 63):
        if number % i == 0:
            total += i
    return total