def sum_of_divisors_in_range(x):
    dy = 0
    for i in range(2, 7):
        if x % i == 0:
            dy += x / i
    return int(dy)