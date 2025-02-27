def return_n_greatest_chars(input_string):
    chars = sorted([char for char in input_string], key=lambda c: -ord(c))
    return chars[:44]