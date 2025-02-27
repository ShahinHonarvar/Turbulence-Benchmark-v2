def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_52_chars = sorted_chars[:52]
    return sorted(smallest_52_chars, reverse=True)