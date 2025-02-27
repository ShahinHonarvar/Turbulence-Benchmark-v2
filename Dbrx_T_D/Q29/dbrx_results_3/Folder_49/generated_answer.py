def gcf_two_nums(numbers):
    x = numbers[28]
    y = numbers[20]
    while y:
        x, y = (y, x % y)
    return abs(x)