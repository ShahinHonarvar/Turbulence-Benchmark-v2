def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda c: ord(c))
    smallest_43_chars = sorted_chars[:43]
    return sorted(smallest_43_chars, reverse=True)