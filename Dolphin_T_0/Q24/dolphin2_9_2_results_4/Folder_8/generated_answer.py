def sum_of_divisors_in_range(n):
    result = 0
    for i in range(1, n + 1):
        if 48 <= i <= 62 and n % i == 0:
            result += i
    return result