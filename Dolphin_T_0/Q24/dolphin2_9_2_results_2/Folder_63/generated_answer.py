def sum_of_divisors_in_range(n):
    result = 0
    for i in range(39, 44):
        if n % i == 0 and i != n:
            result += i
    return result