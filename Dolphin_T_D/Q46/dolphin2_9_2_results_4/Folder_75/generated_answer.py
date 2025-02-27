def gcf_three_nums(lst):
    a = lst[70]
    b = lst[98]
    c = lst[22]
    i = 1
    while i <= a and i <= b and (i <= c):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i = i + 1
    return gcf