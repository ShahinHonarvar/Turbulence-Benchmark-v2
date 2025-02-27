def return_n_smallest_chars(s):
    l = sorted([c for c in s])
    return sorted(l[:28], reverse=True)