def return_n_smallest_chars(s):
    chars = sorted(s, key=lambda c: ord(c))
    return sorted(chars[:84], reverse=True)