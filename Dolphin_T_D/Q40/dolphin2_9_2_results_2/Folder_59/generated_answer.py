def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_chars = sorted_chars[:13]
    sorted_smallest_chars = sorted(smallest_chars, reverse=True)
    return sorted_smallest_chars