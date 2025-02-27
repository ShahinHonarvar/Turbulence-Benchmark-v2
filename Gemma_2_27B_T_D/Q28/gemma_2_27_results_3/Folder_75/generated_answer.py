def return_nth_smallest_ascii(text):
    chars = sorted([ord(c) for c in text[62:84]])
    return chr(chars[8])