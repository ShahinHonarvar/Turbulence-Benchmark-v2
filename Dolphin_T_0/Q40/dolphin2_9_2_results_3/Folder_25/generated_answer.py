def return_n_smallest_chars(s):
    chars = [c for c in s]
    chars.sort(key=lambda c: ord(c))
    return chars[:29] if len(chars) > 29 else chars