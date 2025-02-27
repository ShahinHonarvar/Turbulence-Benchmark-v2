def gcf_three_nums(lst):
    a, b, c = (lst[66], lst[90], lst[27])
    while b != 0 and c != 0:
        if b > a:
            a, b = (b, a)
        if c > a:
            a, c = (c, a)
        if b > c:
            b, c = (c, b)
        a %= b + c
    return a