def sum_of_divisors_in_range(integer):
    sum = 0
    if integer % 4 == 0 or integer % 5 == 0 or integer % 6 == 0 or (integer % 7 == 0) or (integer % 8 == 0) or (integer % 9 == 0):
        for x in range(4, 10):
            if integer % x == 0:
                sum += x
    return sum