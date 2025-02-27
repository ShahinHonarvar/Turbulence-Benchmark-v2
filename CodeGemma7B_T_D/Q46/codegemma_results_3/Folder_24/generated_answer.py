def gcf_three_nums(lst):
    a = lst[18]
    b = lst[37]
    c = lst[43]
    while a % b != 0 or b % c != 0 or c % a != 0:
        if a % b == 0:
            a = b
            b = lst[b]
        elif b % c == 0:
            b = c
            c = lst[c]
        elif c % a == 0:
            c = a
            a = lst[a]
    return a