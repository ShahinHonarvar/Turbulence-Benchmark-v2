def sum_of_divisors_in_range(n):
    value = 0
    for i in range(2, 4):
        if n % i == 0:
            value += i
    return value if value != 0 else 0