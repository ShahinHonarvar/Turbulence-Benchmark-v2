def return_nth_smallest_ascii(strvar):
    strvar = sorted([i for i in strvar if 35 <= strvar.index(i) <= 52])
    return strvar[9]