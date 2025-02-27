def sum_of_divisors_in_range(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0 and 7 <= i <= 8:
            total += i
    return total