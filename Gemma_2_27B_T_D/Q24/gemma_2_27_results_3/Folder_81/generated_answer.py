def sum_of_divisors_in_range(n):
    sum = 0
    if n % 3 == 0:
        sum += 3
    if n % 4 == 0:
        sum += 4
    return sum