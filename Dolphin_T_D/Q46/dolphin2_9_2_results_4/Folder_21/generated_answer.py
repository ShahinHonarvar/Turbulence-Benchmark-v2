def gcf_three_nums(lst):
    a = lst[412]
    b = lst[932]
    c = lst[337]
    gcf = 1
    if a % b == 0:
        gcf = b
    elif b % a == 0:
        gcf = a
    else:
        for i in range(1, min(a, b)):
            if a % i == 0 and b % i == 0:
                gcf = i
    if gcf % c == 0:
        gcf = gcf
    elif c % gcf == 0:
        gcf = gcf
    else:
        for i in range(1, min(gcf, c)):
            if gcf % i == 0 and c % i == 0:
                gcf = i
    return gcf