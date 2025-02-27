def return_n_smallest_chars(s):
    s = sorted(s)
    return sorted(s[:66], reverse=True)