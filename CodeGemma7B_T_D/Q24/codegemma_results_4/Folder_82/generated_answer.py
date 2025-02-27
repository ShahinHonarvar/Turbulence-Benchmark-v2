def sum_of_divisors_in_range(num):
    """Sum of divisors in range"""
    result = 0
    for i in range(num - 3, num + 1):
        if num % i == 0:
            result += i
    if result == 0:
        return 0
    else:
        return result