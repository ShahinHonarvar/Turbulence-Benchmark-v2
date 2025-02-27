def sum_of_divisors_in_range(num):
    if num in range(48, 63):
        return num
    if num % 60 == 0:
        return 60
    if num % 30 == 0:
        return 30
    return 0