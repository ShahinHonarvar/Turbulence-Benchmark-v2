def sum_of_divisors_in_range(n):
    total = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 4 == 0:
            total += i
    return total