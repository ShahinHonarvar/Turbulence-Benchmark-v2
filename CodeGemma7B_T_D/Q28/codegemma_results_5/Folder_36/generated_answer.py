def return_nth_smallest_ascii(str_input):
    str_input = str_input[17:57]
    str_input = sorted(set(str_input))
    return str_input[8]