def return_n_greatest_chars(string):
    chars = list(set(string))
    chars.sort(key=lambda char: ord(char))
    return chars[-2:]