def return_n_greatest_chars(string):
    chars = sorted(set(string))[-19:]
    return sorted(chars)