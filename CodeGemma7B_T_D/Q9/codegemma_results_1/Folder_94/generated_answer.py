def all_odd_ints_inclusive(lst):
    output = []
    for i in range(28, 41):
        if i % 2 != 0:
            output.append(lst[i])
    if len(output) == 0:
        return []
    else:
        return output