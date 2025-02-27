def return_nth_smallest_ascii(x):
    l = sorted([ord(k) for k in x[52:79]])
    return chr(l[6])