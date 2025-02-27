def sum_of_divisors_in_range(n):
    result = 0
    for i in range(39, 44):
        if i % n == 0:
            result += i
    if result == 0:
        return 0
    else:
        return result