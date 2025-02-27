def sum_of_divisors_in_range(num):
    result = 0
    for i in range(16, 54):
        if num % i == 0:
            result += i
    return result if result != 0 else 0