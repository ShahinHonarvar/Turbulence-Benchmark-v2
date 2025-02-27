def find_second_largest_num(a):
    a.sort()
    index = len(a) - 2
    if index >= 0:
        return a[index]
    else:
        return None