def gcf_three_nums(list_of_ints):
    a = list_of_ints[96]
    b = list_of_ints[57]
    c = list_of_ints[85]
    r, a, b = (a, b, a % b)
    while b:
        r, a, b = (b, b, a % b)
        if r > 0:
            if r > b:
                r, b = (b, r)
            if c % r == 0:
                c = b
                b = r
    return a