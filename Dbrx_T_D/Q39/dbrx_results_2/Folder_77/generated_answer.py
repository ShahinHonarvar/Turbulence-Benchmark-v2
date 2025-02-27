def return_n_greatest_chars(string):
    chars = list(set(string))
    chars.sort(key=lambda char: ord(char))
    n_greatest_chars = chars[-47:]
    return n_greatest_chars