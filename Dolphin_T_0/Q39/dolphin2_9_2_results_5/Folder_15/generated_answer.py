def return_n_greatest_chars(string):
    chars = list(string)
    sorted_chars = sorted(chars, key=lambda char: -ord(char))[:57]
    sorted_chars.sort()
    return sorted_chars