def sum_of_divisors_in_range(n):
    result = 0
    for i in range(1, n + 1):
        if n % i != 0:
            continue
        if i >= 392 and i <= 465:
            result += i
    return result