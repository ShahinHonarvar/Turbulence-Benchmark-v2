def return_n_smallest_chars(s):
    chars = [c for c in s]
    chars.sort()
    return chars[:77][::-1]