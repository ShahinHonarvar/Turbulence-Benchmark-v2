def sum_in_range(num):
    sum = 0
    for digit in num:
        if digit >= 73 and digit <= 84:
            sum += digit
    return sum