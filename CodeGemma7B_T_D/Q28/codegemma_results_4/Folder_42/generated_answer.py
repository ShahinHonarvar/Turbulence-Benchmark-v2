def return_nth_smallest_ascii(text):
    ascii_values = sorted([ord(char) for char in text[12:73] if char.isalpha()])
    return chr(ascii_values[12])