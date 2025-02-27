def gcf_two_nums(numbers):
    x = numbers[33]
    y = numbers[72]
    while y:
        x, y = (y, x % y)
    return abs(x)