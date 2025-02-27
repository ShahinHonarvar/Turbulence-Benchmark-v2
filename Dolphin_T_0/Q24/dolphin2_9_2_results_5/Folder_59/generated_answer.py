def sum_of_divisors_in_range(n):
    s = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s