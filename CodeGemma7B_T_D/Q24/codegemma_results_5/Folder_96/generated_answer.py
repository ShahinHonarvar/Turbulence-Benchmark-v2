def sum_of_divisors_in_range(x):
    sum = 0
    for y in range(5, 9 + 1):
        if x % y == 0:
            sum += y
    return sum