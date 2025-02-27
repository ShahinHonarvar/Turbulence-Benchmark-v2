def sum_of_divisors_in_range(n):
    total = 0
    if n <= 2:
        return 0
    for i in range(3, 10, 1):
        if n % i == 0:
            total += i
    if total == 0:
        return 0
    return total