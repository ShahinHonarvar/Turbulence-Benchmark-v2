def find_divisors_in_range(n):
    result = []
    for i in range(2, n + 1):
        if n % i == 0 and 5 <= i <= 8:
            result.append(i)
    return result