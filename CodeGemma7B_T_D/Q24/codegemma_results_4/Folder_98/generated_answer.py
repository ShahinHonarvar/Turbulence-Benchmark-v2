def sum_of_divisors_in_range(n):
    if n <= 1:
        return 0
    result = 1
    for i in range(2, 9):
        if n % i == 0:
            result += i
    return result