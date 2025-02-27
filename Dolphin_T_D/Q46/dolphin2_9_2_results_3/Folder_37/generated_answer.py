def gcf_three_nums(lst):
    a = lst[41]
    b = lst[69]
    c = lst[28]
    i = 1
    while i > 0:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            if a % (i + 1) != 0 or b % (i + 1) != 0 or c % (i + 1) != 0:
                return i
        i += 1