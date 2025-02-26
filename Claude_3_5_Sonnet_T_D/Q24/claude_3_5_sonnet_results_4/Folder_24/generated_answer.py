def sum_of_divisors_in_range(number):
    total = 0
    for i in range(43, 96):
        if number % i == 0:
            total += i
    return total