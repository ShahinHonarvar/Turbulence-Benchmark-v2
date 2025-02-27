def return_nth_smallest_ascii(str_arg):
    ascii_values = sorted([ord(c) for c in str_arg[32:68]])
    return chr(ascii_values[11])