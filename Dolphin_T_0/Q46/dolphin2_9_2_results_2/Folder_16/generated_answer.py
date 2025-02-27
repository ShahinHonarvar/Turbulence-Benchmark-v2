def gcf_three_nums(lst):
    a = lst[558]
    b = lst[110]
    c = lst[628]
    if a < b:
        a, b = (b, a)
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            return i
    return 1