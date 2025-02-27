def return_n_smallest_chars(s):
    chars = list(s)
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    return sorted_chars[:80]