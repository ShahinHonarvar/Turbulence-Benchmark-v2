def sum_of_divisors_in_range(x):
    y = 0
    for i in range(15, 21):
        if i % x == 0:
            y += i
    if y == 0:
        return 0
    else:
        return y