def return_nth_smallest_ascii(char_string):
    ascii_values = [ord(char) for char in char_string if char_string.index(char) in range(14)]
    ascii_values.sort()
    return chr(ascii_values[13])