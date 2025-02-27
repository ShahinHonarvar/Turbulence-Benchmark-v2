def return_nth_smallest_ascii(text):
    ascii_values = sorted([ord(c) for c in text[0:14]])
    return chr(ascii_values[13])