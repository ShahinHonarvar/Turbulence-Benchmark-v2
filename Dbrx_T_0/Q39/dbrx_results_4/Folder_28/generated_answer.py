def return_n_greatest_chars(string):
    chars = list(set(string))
    chars.sort(key=lambda char: ord(char), reverse=True)
    return chars[:3]