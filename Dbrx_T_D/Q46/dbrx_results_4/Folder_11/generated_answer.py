def gcf_three_nums(numbers):
    a = numbers[37]
    b = numbers[30]
    c = numbers[48]
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return abs(a)