def sum_of_divisors_in_range(n):
    if n < 1:
        return 0
    result = 0
    if 19 <= n <= 69:
        for i in range(1, n + 1):
            if n % i == 0:
                result += i
    return result