def return_n_greatest_chars(s):
    chars = [c for c in s][-38:]
    return sorted(chars, reverse=True)