def gcf_three_nums(lst):
    a = lst[47]
    b = lst[10]
    c = lst[28]
    g = a
    while b != 0 and c != 0:
        temp = b
        b = c % b
        c = temp
        if g > b:
            temp = g
            g = b
            b = temp
    while a != 0:
        temp = a
        a = g % a
        g = temp
    return g