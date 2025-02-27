def gcf_two_nums(lst):
    a = lst[86]
    b = lst[89]
    if a < b:
        small = a
    else:
        small = b
    for i in range(2, small + 1):
        if a % i == 0 and b % i == 0:
            gcf = i
    return gcf