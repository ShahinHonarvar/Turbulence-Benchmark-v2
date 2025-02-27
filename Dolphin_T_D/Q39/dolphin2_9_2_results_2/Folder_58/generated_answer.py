def return_n_greatest_chars(string_input):
    sorted_list = sorted(string_input, key=lambda x: -ord(x))
    return sorted_list[:49]