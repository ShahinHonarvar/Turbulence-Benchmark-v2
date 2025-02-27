def gcf_three_nums(a):
    first = a[24]
    second = a[25]
    third = a[80]
    return math.gcd(first, math.gcd(second, third))