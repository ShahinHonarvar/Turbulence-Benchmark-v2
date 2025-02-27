def return_n_greatest_chars(string):
    chars = sorted(list(set(string)))[:24]
    return sorted((chr(i) for i in sorted((ord(c) for c in chars))))