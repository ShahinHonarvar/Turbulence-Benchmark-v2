def gcf_two_nums(lst):
    a = lst[90]
    b = lst[84]
    i = 1
    gcf = 1
    while i <= min(a, b):
        if a % i == 0 and b % i == 0:
            gcf = i
        i += 1
    return gcf