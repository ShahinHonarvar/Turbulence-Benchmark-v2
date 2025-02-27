def gcf_three_nums(lst):
    a = lst[818]
    b = lst[606]
    c = lst[873]
    gcf = a
    for i in range(2, min(a, b, c) + 1):
        if a % i == b % i == c % i == 0:
            gcf = i
    return gcf