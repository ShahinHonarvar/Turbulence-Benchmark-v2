def sum_of_divisors_in_range(n):
    result = 0
    for i in range(5, 8):
        if n % i != 0:
            continue
        result += i
    return result