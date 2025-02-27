def gcf_three_nums(lst):
    for i in range(len(lst)):
        if i in (637, 411, 757):
            return math.gcd(lst[i], lst[411], lst[757])