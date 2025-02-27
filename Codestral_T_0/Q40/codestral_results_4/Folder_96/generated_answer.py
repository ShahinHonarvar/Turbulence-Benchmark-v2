def return_n_smallest_chars(s):
    return sorted(sorted(s)[:20])[::-1]