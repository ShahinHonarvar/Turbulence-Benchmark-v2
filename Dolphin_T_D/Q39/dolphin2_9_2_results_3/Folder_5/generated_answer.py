def return_n_greatest_chars(input_str):
    sorted_chars = sorted(list(input_str), key=lambda x: -ord(x))
    return sorted_chars[:46]