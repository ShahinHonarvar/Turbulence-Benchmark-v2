def return_nth_smallest_ascii(char_string):
    ascii_values = sorted((ord(char) for char in char_string if 0 <= char_string.index(char) <= 87))[:14]
    return ascii_values[13] if len(ascii_values) >= 14 else None