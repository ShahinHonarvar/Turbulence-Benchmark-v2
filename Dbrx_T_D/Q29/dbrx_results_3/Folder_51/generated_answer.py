def gcf_two_nums(numbers):
    x = numbers[46]
    y = numbers[84]
    while y:
        x, y = (y, x % y)
    return abs(x)