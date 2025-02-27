def return_n_greatest_chars(input_string):
    sorted_chars = sorted(list(input_string), key=lambda x: -ord(x))
    return sorted_chars[:2]