def sum_of_divisors_in_range(n):
    result = 0
    for i in range(max(4, 0), min(9, n) + 1):
        if n % i == 0:
            result += i
    return result