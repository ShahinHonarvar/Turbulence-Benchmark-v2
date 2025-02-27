def return_n_smallest_chars(s):
    chars = sorted(s)
    return sorted(chars[:46], reverse=True)