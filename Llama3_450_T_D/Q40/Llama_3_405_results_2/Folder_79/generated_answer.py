def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda c: ord(c))
    n_smallest_chars = sorted_chars[:82]
    return sorted(n_smallest_chars, reverse=True)