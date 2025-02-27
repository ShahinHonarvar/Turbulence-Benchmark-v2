def return_nth_smallest_ascii(char_string):
    ascii_values = [ord(char) for char in char_string[51:79] if char not in char_string[:51] + char_string[78:]]
    ascii_values.sort()
    return chr(ascii_values[9])