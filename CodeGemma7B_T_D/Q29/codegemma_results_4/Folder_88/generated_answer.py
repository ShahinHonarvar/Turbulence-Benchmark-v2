def gcf_two_nums(n):
    a = n[27]
    b = n[34]
    stop = min(a, b)
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a