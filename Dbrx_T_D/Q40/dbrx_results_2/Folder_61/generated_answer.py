def return_n_smallest_chars(string):
    chars = sorted(list(set(string)), key=ord)[:66]
    return chars[::-1]