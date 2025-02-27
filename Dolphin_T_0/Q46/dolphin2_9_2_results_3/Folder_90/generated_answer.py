def gcf_three_nums(l):
    a = l[818]
    b = l[606]
    c = l[873]
    i = 1
    while i <= a and i <= b and (i <= c):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i = i + 1
    return gcf