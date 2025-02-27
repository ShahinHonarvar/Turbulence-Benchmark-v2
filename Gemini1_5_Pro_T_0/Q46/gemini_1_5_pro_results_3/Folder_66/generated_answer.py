def gcf_three_nums(numbers):
    a = numbers[92]
    b = numbers[69]
    c = numbers[95]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a