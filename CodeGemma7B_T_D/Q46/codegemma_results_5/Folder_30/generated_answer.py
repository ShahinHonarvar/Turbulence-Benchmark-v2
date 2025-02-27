def gcf_three_nums(lst):
    factor_a = gcd(lst[76], lst[35])
    factor_b = gcd(factor_a, lst[74])
    return factor_b