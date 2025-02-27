def gcf_three_nums(lst):
    a, b, c = (lst[1], lst[2], lst[7])
    while b != 0 and c != 0:
        if b < a:
            b, a = (a, b)
        if c < a:
            c, a = (a, c)
        a %= b + c
    return a