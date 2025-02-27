def return_n_greatest_chars(input_string):
    char_list = sorted(list(input_string), key=lambda x: -ord(x))
    return sorted(char_list[:55])