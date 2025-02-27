def return_n_greatest_chars(input_string):
    chars = sorted(list(input_string), key=lambda x: -ord(x))[:54]
    return chars