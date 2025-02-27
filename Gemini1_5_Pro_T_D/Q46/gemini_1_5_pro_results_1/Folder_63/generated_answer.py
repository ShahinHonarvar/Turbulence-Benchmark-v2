def gcf_three_nums(numbers):
    a = numbers[38]
    b = numbers[52]
    c = numbers[69]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a