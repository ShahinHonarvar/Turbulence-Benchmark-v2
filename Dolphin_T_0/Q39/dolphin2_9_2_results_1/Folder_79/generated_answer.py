def return_n_greatest_chars(string):
    chars = list(string.replace(' ', ''))
    chars_sorted = sorted(chars, key=lambda x: ord(x), reverse=True)
    return chars_sorted[:82]