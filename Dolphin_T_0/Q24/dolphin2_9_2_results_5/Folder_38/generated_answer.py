def sum_of_divisors_in_range(num):
    result = 0
    for i in range(16, 69):
        if num % i == 0:
            result += i
    return result