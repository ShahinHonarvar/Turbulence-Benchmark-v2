def sum_of_divisors_in_range(num):
    if num < 16 or num > 68:
        return 0
    result = 0
    for i in range(16, 69):
        if num % i == 0:
            result += i
    return result