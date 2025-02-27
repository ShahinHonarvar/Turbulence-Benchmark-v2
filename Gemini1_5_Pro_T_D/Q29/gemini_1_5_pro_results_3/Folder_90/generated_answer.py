def gcf_two_nums(l):
    a = l[634]
    b = l[585]
    while b:
        a, b = (b, a % b)
    return a