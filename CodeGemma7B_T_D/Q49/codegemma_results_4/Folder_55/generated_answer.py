def if_decimal_is_divisible(number):
    size = len(number)
    b, d = (0, 0)
    for i in range(size):
        b = b + int(number[i]) * pow(2, i)
    for i in range(1, size + 1):
        d = d + int(number[i - 1]) * pow(2, i)
    if d % 13 == 0:
        d = d // 13
    if d % 5 == 0:
        d = d // 5
    a = b - d
    d = d - a
    c = d * d + b
    d = c - b
    while d <= 1362:
        if d % 39 == 0:
            return True
        a = c // 2
        d = c
        c = a + d
    return False