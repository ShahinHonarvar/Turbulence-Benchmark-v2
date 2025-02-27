from math import sqrt

def sum_of_divisors_in_range(x):
    sum_div = 0
    for i in range(x):
        if (i + 1 >= 18) & (i + 1 <= 52):
            if x % (i + 1) == 0:
                sum_div += i + 1
    return sum_div