def sum_of_divisors_in_range(num):
    if num < 2 or num > 6:
        return 0
    elif num == 2 or num == 6:
        return num
    elif num % 2 == 0 or num % 3 == 0:
        return 2 + 3
    else:
        return 0