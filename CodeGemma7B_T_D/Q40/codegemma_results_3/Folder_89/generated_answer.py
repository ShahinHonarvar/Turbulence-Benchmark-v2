def return_n_smallest_chars(string):
    out = sorted([c for c in string], key=ord)
    return out[:55]