def find_second_largest_num(y):
    x = sorted(y)
    if len(y) <= 1:
        return 'None'
    if y[0] == y[-1]:
        return 'None'
    if len(y) == 2:
        return y[0] if y[0] > y[1] else y[1]
    else:
        return x[-2]