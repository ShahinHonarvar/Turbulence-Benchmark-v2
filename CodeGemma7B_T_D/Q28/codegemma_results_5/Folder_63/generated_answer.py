def return_nth_smallest_ascii(text):
    text = text[47:71]
    ascii_values = sorted([ord(char) for char in text])
    return chr(ascii_values[13])