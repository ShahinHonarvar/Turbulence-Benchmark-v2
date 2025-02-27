def return_nth_smallest_ascii(char_string):
    ascii_values = [ord(char) for char in set(char_string[14:55])]
    ascii_values.sort()
    if len(ascii_values) < 11:
        return None
    else:
        return chr(ascii_values[10])