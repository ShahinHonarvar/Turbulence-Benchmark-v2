def gcf_three_nums(lst):
    a = lst[87]
    b = lst[20]
    c = lst[36]
    if a == 0:
        return b + c
    elif b == 0:
        return a + c
    elif c == 0:
        return a + b
    else:
        while b > 0 and c > 0:
            if b > c:
                b %= a
            else:
                c %= a
        return a * (b + c)