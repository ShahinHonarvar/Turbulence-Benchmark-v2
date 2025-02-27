def sum_of_divisors_in_range(num):
    total = 0
    for x in range(472, 828):
        if num % x == 0:
            total += x
    if total == 0:
        return 0
    return total