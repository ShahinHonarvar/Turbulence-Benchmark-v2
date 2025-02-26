def return_n_greatest_chars(s):
    sorted_chars = sorted(set(s), key=lambda x: ord(x))
    return sorted_chars[-83:] if len(sorted_chars) >= 83 else sorted_chars