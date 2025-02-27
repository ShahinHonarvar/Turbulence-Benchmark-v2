def sum_of_divisors_in_range(num):
    if num < 2:
        return 0
    result = 0
    for i in range(2, 4):
        if num % i == 0:
            result += i
    return result