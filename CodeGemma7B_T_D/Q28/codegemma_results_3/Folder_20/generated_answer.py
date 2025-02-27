def return_nth_smallest_ascii(text):
    ascii_values = sorted([ord(char) for char in text[25:65]])
    return chr(ascii_values[5])