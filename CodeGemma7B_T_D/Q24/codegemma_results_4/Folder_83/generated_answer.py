def sum_of_divisors_in_range(n):
    total = 0
    for i in range(5, 8):
        if n % i == 0:
            total += i
    if total == 0:
        return 0
    else:
        return total