def return_n_smallest_chars(s):
    chars = sorted(sorted(s, key=ord)[:79], reverse=True)
    return chars