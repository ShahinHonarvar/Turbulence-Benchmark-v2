def return_n_smallest_chars(s):
    return sorted([ord(c) for c in s])[:52][::-1]