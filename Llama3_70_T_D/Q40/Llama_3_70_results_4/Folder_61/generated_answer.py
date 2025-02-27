def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda c: (ord(c), s.index(c)))
    return sorted(sorted_chars[:66], reverse=True)