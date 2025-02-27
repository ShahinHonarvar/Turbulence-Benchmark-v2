def return_n_smallest_chars(string):
    chars = sorted(list(set(string)))[:3]
    return chars