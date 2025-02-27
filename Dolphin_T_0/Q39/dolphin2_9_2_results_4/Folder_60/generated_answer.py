def return_n_greatest_chars(input_string):
    chars = list(input_string)
    chars.sort(key=lambda c: -ord(c))
    return chars[:28]