def gcf_three_nums(lst):
    a, b, c = (lst[4], lst[0], lst[8])
    return math.gcd(math.gcd(a, b), c)