def return_n_greatest_chars(input_string):
    return sorted(input_string, key=lambda x: -ord(x))[:68]