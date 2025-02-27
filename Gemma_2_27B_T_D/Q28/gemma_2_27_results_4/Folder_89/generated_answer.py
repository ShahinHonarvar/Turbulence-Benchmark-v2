def return_nth_smallest_ascii(text):
    chars = sorted([ord(c) for c in text[24:72]])
    return chr(chars[7])