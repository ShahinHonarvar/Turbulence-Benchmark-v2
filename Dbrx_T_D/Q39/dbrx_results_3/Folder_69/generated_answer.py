def return_n_greatest_chars(input_string):
    input_string = sorted(input_string, key=ord, reverse=True)
    return input_string[:65]