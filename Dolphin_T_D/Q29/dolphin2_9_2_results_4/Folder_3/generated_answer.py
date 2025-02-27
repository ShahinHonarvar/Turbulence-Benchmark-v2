def gcf_two_nums(lst):
    a = lst[47]
    b = lst[10]
    i = min(a, b)
    gcf = 1
    while i > 1:
        if a % i == 0 and b % i == 0:
            gcf = i
            break
        i -= 1
    return gcf