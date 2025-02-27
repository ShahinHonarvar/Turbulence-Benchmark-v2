def sum_of_divisors_in_range(number):
    result = 0
    for i in range(35, 38):
        if number % i == 0:
            result += i
    return result