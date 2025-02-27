def sum_of_divisors_in_range(n):
    result = 0
    for i in range(1, n + 1):
        if n % i == 0 and 43 <= i <= 77:
            result += i
    if result == 0:
        return 0
    else:
        return result