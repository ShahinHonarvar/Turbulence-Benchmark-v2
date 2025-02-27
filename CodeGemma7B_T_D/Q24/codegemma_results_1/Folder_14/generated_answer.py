def sum_of_divisors_in_range(x):
    result = 0
    for i in range(6, 9):
        if x % i == 0:
            result += i
    if result == 0:
        return 0
    else:
        return result