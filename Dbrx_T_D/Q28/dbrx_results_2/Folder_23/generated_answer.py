def return_nth_smallest_ascii(input_string):
    sub_string = input_string[29:48]
    ascii_values = sorted(set((ord(char) for char in sub_string)))
    return chr(ascii_values[6]) if len(ascii_values) > 6 else None