def sum_of_divisors_in_range(n):
    result = 0
    for i in range(42, 78):
        if n % i == 0:
            result += i
    return result