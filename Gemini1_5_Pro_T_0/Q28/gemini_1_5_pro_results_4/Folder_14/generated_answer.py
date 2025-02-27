def return_nth_smallest_ascii(text):
    ascii_values = sorted([ord(char) for i, char in enumerate(text) if 46 <= i <= 82])
    return chr(ascii_values[15])