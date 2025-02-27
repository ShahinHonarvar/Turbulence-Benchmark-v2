def sum_of_divisors_in_range(num):
    return sum((x for x in range(11, 57) if num % x == 0)) or 0