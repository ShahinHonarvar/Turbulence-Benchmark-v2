def find_divisors_in_range(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0 and 8 <= i <= 9:
            result.append(i)
    return result