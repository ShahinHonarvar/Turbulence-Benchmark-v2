def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0
    result = 0
    for i in range(5, 9):
        if n % i == 0:
            result += i
    return result