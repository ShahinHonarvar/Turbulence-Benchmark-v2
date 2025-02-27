def gcf_three_nums(lst):
    gcf = lst[9]
    for i in range(1, min(6, 2) + 1):
        gcf = math.gcd(lst[9 - i], gcf)
    return gcf