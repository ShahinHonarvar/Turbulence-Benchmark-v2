def gcf_three_nums(lst):
    a = lst[90]
    b = lst[84]
    c = lst[47]
    i = 1
    gcf = 1
    while i <= a:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i = i + 1
    return gcf