def return_nth_smallest_ascii(s):
    chars = sorted(set(s))[63:77]
    return min(chars, key=ord)[13]