def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(c) for c in set(input_string[50:77])]
    ascii_values.sort()
    return chr(ascii_values[10]) if len(ascii_values) > 10 else None