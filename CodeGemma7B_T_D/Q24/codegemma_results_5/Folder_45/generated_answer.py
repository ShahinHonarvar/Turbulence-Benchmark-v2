def sum_of_divisors_in_range(n):
    result = 0
    for i in range(4, min(n, 8) + 1):
        if n % i == 0:
            result += i
    return result