def sum_of_divisors_in_range(n):
    sum = 0
    if n % 1 == 0:
        sum += 1
    if n % 2 == 0:
        sum += 2
    return sum