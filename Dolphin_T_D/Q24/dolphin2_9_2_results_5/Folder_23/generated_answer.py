def sum_of_divisors_in_range(n):
    result = 0
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n - 1) // 2 + 1
    for i in range(18, 53):
        if i <= n:
            result += i
    return result