def gcf_three_nums(numbers):
    a = numbers[477]
    b = numbers[696]
    c = numbers[663]
    while True:
        if a == b == c == 0:
            return 0
        if a == 0:
            return b if b <= c else c
        if b == 0:
            return a if a <= c else c
        if c == 0:
            return a if a <= b else b
        if a < b:
            a, b = (b, a)
        if b < c:
            b, c = (c, b)
        a = a % b
        b = b % c