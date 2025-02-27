def gcf_three_nums(lst):
    gcf = int(lst[20])
    for i in range(21, 63):
        gcf = int(gcf * lst[i] / math.gcd(gcf, lst[i]))
    return gcf