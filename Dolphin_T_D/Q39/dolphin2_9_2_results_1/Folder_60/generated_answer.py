def return_n_greatest_chars(input_string):
    chars = [char for char in input_string]
    chars.sort(key=lambda char: -ord(char))
    return chars[:28]