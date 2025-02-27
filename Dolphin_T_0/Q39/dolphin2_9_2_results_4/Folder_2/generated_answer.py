def return_n_greatest_chars(s):
    chars = [c for c in s if c.isalpha()]
    chars.sort(reverse=True)
    return chars[:48]