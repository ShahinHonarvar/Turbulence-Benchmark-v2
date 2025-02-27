def return_nth_smallest_ascii(text):
    ascii_codes = sorted([ord(text[i]) for i in range(18)])
    return chr(ascii_codes[17])