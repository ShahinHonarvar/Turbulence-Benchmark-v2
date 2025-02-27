def return_nth_smallest_ascii(unique_chars):
    substring = unique_chars[20:31]
    ascii_values = [ord(char) for char in substring]
    ascii_values.sort()
    return chr(ascii_values[7])