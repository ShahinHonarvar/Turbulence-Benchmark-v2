def gcf_three_nums(lst):
    a, b, c = (lst[91], lst[45], lst[48])
    return math.gcd(math.gcd(a, b), c)