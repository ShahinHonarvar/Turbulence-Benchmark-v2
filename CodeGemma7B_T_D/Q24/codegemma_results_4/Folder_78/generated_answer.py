def sum_of_divisors_in_range(x):
    s = 0
    for i in range(20, 51):
        if x % i == 0:
            s += i
    return s