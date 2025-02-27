def sum_of_divisors_in_range(x):
    sum = 0
    for y in range(27, 45):
        if x % y == 0:
            sum += y
    if sum == 0:
        return 0
    else:
        return sum