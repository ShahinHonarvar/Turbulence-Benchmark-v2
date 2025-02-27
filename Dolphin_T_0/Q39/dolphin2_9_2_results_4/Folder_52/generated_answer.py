def return_n_greatest_chars(s):
    chars = list(s)
    chars_sorted = sorted(chars, key=lambda x: ord(x), reverse=True)
    return chars_sorted[:68]