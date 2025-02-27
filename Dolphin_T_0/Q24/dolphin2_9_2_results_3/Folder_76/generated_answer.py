def sum_of_divisors_in_range(n):
    result = 0
    for i in range(744, 886):
        if n % i == 0 and i != n:
            result += i
    return result