def return_nth_smallest_ascii(text):
    substring = text[32:68]
    ascii_values = sorted([ord(char) for char in substring])
    return chr(ascii_values[11])