def gcf_three_nums(numbers):
    a = numbers[40]
    b = numbers[15]
    c = numbers[99]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a