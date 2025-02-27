def return_n_smallest_chars(s):
    return sorted(sorted(s)[:34]) if len(s) >= 34 else sorted(s)