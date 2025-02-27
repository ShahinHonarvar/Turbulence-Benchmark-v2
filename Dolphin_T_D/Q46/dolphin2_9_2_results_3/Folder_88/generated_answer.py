def gcf_three_nums(numbers):
    a = numbers[47]
    b = numbers[10]
    c = numbers[28]
    factor = a
    while factor > 1:
        if a % factor == 0 and b % factor == 0 and (c % factor == 0):
            return factor
        factor -= 1
    return 1