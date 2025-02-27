def sum_of_divisors_in_range(x):
    total = 0
    for i in range(6, 9):
        if x % i == 0:
            total += i
    if total == 0:
        return 0
    else:
        return total