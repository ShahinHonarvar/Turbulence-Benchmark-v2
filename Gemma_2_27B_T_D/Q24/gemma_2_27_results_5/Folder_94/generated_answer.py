def sum_of_divisors_in_range(n):
    sum = 0
    if 35 <= n <= 37:
        sum += n
    elif n % 35 == 0:
        sum += 35
    elif n % 36 == 0:
        sum += 36
    elif n % 37 == 0:
        sum += 37
    return sum