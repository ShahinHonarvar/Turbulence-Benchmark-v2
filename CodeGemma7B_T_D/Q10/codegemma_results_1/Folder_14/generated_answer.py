def list(all_odd_ints_exclusive):
    list = []
    for i in range(1, 8):
        if i % 2 != 0:
            list.append(i)
    return list