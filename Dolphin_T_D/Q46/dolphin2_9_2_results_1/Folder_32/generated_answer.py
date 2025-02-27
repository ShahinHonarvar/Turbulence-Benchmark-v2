def gcf_three_nums(lst):
    a = lst[20]
    b = lst[43]
    c = lst[95]
    i = 1
    while i <= min(a, b, c):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf