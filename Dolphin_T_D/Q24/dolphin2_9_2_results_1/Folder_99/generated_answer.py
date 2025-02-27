def sum_of_divisors_in_range(number):
    result = 0
    for i in range(378, 783):
        if number % i == 0:
            result += i
    return result