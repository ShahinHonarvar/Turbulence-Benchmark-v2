def return_n_smallest_chars(string):
    chars = sorted([char for char in string], key=ord)
    return chars[:2]