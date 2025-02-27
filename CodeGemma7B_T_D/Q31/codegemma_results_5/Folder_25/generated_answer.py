def if_perfect_num(a):
    if sum((i for i in range(1, a[90] + 1))) == a[90]:
        return True
    else:
        return False