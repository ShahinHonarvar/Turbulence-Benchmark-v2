def filter_chars(a):
    for ic in range(2, 7):
        farray = list(a)
        farray[ic] = None
        a = ''.join(farray)
    return a