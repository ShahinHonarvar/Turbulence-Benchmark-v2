def gcf_three_nums(lst):
    a = lst[40]
    b = lst[15]
    c = lst[99]
    i = 1
    gcf = 1
    while i <= min(a, b, c):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf