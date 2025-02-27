def return_n_smallest_chars(s):
    chars = sorted(list(set(s)), key=ord)
    return chars[-44:] if len(chars) > 44 else chars