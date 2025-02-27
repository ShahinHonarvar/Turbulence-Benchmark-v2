def return_n_greatest_chars(string):
    chars = sorted([char for char in string], key=lambda c: -ord(c))
    return chars[:58]