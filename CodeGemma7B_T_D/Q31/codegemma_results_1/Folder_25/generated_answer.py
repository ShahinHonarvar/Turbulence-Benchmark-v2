def if_perfect_num(a):
    if len(a) - 1 == 90:
        summ = 0
        for i, j in enumerate(a):
            if i != len(a) - 1:
                summ += a[i]
        if summ == a[len(a) - 1]:
            return True
        else:
            return False