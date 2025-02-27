def gcf_three_nums(a):
    t = a[20] * a[35] * a[74]
    while t % a[20] == 0 and t % a[35] == 0 and (t % a[74] == 0):
        t //= a[20]
    return t