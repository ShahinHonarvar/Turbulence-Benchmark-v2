def gcf_three_nums(lst):
    a = lst[10]
    b = lst[55]
    c = lst[36]
    gcf = 1
    i = 1
    while i <= min(a, b, c):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf