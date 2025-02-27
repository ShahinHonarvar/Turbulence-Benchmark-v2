def gcf_three_nums(lst):
    a = lst[33]
    b = lst[78]
    c = lst[93]
    i = 1
    gcf = 1
    while i <= a and i <= b and (i <= c):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        i += 1
    return gcf