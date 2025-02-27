def if_perfect_num(a):
    if a[94] % 2 == 0 and a[94] // 2 in a[:94]:
        return True
    else:
        return False