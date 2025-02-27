def return_nth_smallest_ascii(text):
    values = sorted([ord(c) for c in text[34:69]])
    return chr(values[5])