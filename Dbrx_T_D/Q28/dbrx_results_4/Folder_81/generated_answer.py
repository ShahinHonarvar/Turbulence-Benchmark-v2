def return_nth_smallest_ascii(char_string):
    ascii_values = [ord(char) for char in char_string if char_string.index(char) <= 13]
    ascii_values = sorted(list(set(ascii_values)))
    return chr(ascii_values[13])