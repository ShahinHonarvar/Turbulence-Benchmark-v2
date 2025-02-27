def gcf_three_nums(lst):
    a, b, c = (lst[99], lst[63], lst[74])
    while b != 0 and c != 0:
        if a > b and a > c:
            a %= b + c
        elif b > a and b > c:
            b %= a + c
        else:
            c %= a + b
    return a + b + c