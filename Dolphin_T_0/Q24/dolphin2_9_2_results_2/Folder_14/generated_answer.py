def sum_of_divisors_in_range(num):
    result = 0
    for i in range(6, 9):
        if num % i == 0:
            result += i
    return result if result != 0 else 0