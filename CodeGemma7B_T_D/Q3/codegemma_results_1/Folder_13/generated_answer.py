def all_pos_ints_inclusive(list):
    output = []
    for n in list:
        if n > 0 and n >= 25 and (n <= 87):
            output.append(n)
    return output