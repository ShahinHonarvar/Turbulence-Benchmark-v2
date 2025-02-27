def if_decimal_is_divisible(s):
    l = list(map(int, s))
    a, b = (0, 1)
    fn = 1
    while True:
        a1 = a + b
        for num in l:
            fn *= num
        if fn % a1 == 0:
            return True
        a, b = (b, a + b)
        l.pop()
        if not l:
            return False