def find_original_set(a, b, c, d, e):
    temp1 = a | b
    temp2 = temp1 | c
    temp3 = temp2 | d
    temp4 = temp3 | e
    return temp4