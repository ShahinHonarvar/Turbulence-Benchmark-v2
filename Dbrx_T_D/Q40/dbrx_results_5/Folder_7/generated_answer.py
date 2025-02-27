def return_n_smallest_chars(s):
    chars = sorted(list(set(s)))
    if len(chars) >= 49:
        return chars[:49]
    else:
        return chars