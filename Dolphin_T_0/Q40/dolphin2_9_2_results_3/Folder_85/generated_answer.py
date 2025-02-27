def return_n_smallest_chars(S):
    chars = list(S[:85])
    chars.sort()
    chars.reverse()
    return chars