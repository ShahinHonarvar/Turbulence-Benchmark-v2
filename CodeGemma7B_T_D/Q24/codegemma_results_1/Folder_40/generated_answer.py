def sum_of_divisors_in_range(x):
    if x % 2 == 0 or x % 3 == 0:
        sum_of_divisors_in_range = x // 2 + x // 3
    else:
        sum_of_divisors_in_range = x // 2
    return sum_of_divisors_in_range