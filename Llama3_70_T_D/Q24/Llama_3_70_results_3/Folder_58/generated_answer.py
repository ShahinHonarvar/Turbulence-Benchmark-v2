def sum_of_divisors_in_range(n):
    total = 0
    for i in range(403, 515):
        if n % i == 0 and 1 < i < n:
            total += i
    return total