def return_n_smallest_chars(s):
    s = sorted(s)
    return sorted(s[:90], reverse=True)