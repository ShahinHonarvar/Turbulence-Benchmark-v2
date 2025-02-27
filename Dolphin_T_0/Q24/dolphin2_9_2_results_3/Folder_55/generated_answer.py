def sum_of_divisors_in_range(n):
    total = 0
    for i in range(1, n + 1):
        if i in range(5, 9) and n % i == 0:
            total += i
    return total