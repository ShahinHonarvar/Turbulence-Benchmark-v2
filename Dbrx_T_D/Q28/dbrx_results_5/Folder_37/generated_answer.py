def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(c) for c in input_string[28:68] if c != ' ']
    ascii_values.sort()
    if len(ascii_values) >= 15:
        return chr(ascii_values[14])
    else:
        return None