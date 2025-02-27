def return_n_greatest_chars(s):
    chars = list(s)
    chars.sort(reverse=True, key=lambda e: ord(e))
    return chars[:84]