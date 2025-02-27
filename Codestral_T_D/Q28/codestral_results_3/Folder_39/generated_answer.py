def return_nth_smallest_ascii(string):
    ascii_values = sorted((ord(char) for char in string[1:67] if char.isascii()))
    return chr(ascii_values[7]) if len(ascii_values) > 7 else None