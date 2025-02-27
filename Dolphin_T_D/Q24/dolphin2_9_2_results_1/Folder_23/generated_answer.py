def sum_of_divisors_in_range(num):
    result = 0
    for i in range(18, 53):
        if num % i == 0:
            result += i
    return result