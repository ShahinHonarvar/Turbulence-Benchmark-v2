def return_n_greatest_chars(input_string):
    input_string = sorted(set(input_string), key=input_string.index)
    return input_string[:27]