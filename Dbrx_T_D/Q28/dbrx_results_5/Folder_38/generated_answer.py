def return_nth_smallest_ascii(input_string):
    ascii_chars = sorted(input_string)[0:46]
    tenth_smallest_char = sorted(ascii_chars.keys())[9]
    return tenth_smallest_char