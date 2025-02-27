def return_n_smallest_chars(string):
    smallest_chars = sorted([char for char in string], key=lambda x: (ord(x), string.index(x)))
    return sorted(smallest_chars[:20], reverse=True)