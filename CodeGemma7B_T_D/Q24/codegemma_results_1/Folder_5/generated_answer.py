def sum_of_divisors_in_range(num):
    if num % 7 == 0 or num % 8 == 0:
        return num
    else:
        return 0