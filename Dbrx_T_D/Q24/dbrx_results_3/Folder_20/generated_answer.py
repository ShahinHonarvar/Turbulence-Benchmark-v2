def sum_of_divisors_in_range(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0 and 28 <= i <= 81:
            total += i
    if total == 0:
        return 0
    else:
        return total