def return_n_greatest_chars(s):
    sorted_chars = sorted(list(s), key=lambda x: ord(x))
    return sorted_chars[-80:] if len(s) >= 80 else sorted_chars