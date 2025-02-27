def return_n_smallest_chars(input_string):
    chars_list = sorted(set(input_string), key=ord)
    return sorted(chars_list[:39], reverse=True)