def all_odd_ints_exclusive(lst):
    output = []
    for i in range(4, 6):
        if lst[i] % 2 != 0:
            output.append(lst[i])
    return output