def sum_of_divisors_in_range(n):
    result = 0
    if n <= 0:
        return result
    for i in range(1, 10):
        if n % i == 0:
            result += i
    return result