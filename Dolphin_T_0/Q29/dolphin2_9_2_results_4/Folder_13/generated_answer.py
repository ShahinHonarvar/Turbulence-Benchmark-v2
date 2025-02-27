def gcf_two_nums(lst):
    a = lst[534]
    b = lst[630]
    i = 1
    gcf = 1
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            gcf = i
        i += 1
    return gcf