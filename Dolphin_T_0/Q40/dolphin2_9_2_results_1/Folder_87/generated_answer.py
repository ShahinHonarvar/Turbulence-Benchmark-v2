def return_n_smallest_chars(s):
    chars = [c for c in s]
    smallest_chars = sorted(chars, key=lambda c: ord(c))[:24]
    return sorted(smallest_chars)