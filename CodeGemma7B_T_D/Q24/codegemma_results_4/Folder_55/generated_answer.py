def sum_of_divisors_in_range(value):
    sum = 0
    for x in range(5, value + 1):
        if value % x == 0:
            sum += x
            if x >= 8:
                break
    return sum or 0