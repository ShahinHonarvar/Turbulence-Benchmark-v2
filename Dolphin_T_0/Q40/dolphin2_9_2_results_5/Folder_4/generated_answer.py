def return_n_smallest_chars(s):
    chars = sorted(s, key=lambda x: ord(x))[:90]
    return sorted(chars, reverse=True)