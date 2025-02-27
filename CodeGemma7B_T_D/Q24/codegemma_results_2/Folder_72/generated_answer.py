def sum_of_divisors_in_range(x):
    total = 0
    for i in range(32, 91):
        if i % x == 0:
            total += i
    return total if total else 0