def gcf_three_nums(lst):
    a = lst[96]
    b = lst[53]
    c = lst[35]
    gcf = 1
    for i in range(1, max(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
    return gcf