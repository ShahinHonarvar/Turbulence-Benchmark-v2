def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_28_chars = sorted_chars[:28]
    return sorted(smallest_28_chars, reverse=True)