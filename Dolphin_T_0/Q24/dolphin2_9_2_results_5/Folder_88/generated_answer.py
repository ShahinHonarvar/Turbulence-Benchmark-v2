def sum_of_divisors_in_range(n):
    result = 0
    for i in range(6, n + 1):
        if n % i == 0:
            result += i
    return result