def sum_of_divisors_in_range(number):
    result = 0
    for x in range(48, 61):
        if number % x == 0:
            result += x
    return result or 0