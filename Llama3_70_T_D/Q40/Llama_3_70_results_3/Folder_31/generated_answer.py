def return_n_smallest_chars(s):
    s = sorted(s)
    return sorted(s[:70], reverse=True)