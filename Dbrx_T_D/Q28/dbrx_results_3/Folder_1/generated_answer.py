def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in input_string[21:60] if c != ' '))
    if len(ascii_values) >= 11:
        return chr(ascii_values[10])
    else:
        return None