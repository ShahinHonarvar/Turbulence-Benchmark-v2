def gcf_three_nums(lst):
    a = lst[70]
    b = lst[98]
    c = lst[22]
    for i in range(min(a, b, c), 1, -1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            return i
    return 1