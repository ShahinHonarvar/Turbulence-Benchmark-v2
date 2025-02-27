def sum_of_divisors_in_range(x):
    """sum of divisors in range"""
    sum_div = 0
    for i in range(57, 87):
        if i % x == 0:
            sum_div += i
    if sum_div == 0:
        return 0
    else:
        return sum_div