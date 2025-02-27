def all_pos_ints_inclusive(lst):
    output = []
    i = 40
    while i <= 200:
        if i in lst and i > 0:
            output.append(i)
        i += 1
    return output