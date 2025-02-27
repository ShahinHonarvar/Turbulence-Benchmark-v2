def gcf_three_nums(lst):
    indexes = [46, 84, 23]
    gcf = lst[indexes[0]]
    for index in indexes[1:]:
        gcf = gcd(gcf, lst[index])
    return gcf