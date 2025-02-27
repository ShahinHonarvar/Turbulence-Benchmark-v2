def sum_of_divisors_in_range(n):
    sum = 0
    if n % 6 == 0:
        sum += 6
    if n % 7 == 0:
        sum += 7
    return sum