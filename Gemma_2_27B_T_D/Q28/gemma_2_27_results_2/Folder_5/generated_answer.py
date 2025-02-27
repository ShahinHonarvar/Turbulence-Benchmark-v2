def return_nth_smallest_ascii(text):
    valid_chars = sorted([ord(c) for c in text[5:90]])
    return chr(valid_chars[12])