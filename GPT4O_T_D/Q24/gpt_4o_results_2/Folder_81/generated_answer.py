def sum_of_divisors_in_range(n):
    if n % 3 == 0 and n % 4 == 0:
        return 7
    elif n % 3 == 0:
        return 3
    elif n % 4 == 0:
        return 4
    else:
        return 0