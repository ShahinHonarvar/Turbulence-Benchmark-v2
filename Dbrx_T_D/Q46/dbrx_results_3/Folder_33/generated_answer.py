def gcf_three_nums(numbers):
    a, b, c = (numbers[252], numbers[149], numbers[564])
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a