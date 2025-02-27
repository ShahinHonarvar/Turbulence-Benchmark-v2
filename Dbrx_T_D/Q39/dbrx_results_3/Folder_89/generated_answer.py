def return_n_greatest_chars(input_string):
    ascii_list = sorted(list(set(input_string)), reverse=True)
    return [chr(i) for i in ascii_list[:55]]