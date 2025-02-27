def gcf_three_nums(lst):
    a = lst[29]
    b = lst[74]
    c = lst[49]
    factors = set((x for a in range(1, min([a, b, c])) if all((n % a == 0 for n in [a, b, c]))))
    return max(factors)