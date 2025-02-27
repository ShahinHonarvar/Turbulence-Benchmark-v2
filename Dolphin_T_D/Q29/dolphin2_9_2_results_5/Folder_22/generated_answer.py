def gcf_two_nums(lst):
    a = lst[24]
    b = lst[68]
    i = 1
    while i <= min(a, b):
        if a % i == 0 and b % i == 0:
            gcf = i
            i += 1
        else:
            i += 1
    return gcf