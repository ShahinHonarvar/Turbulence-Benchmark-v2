def return_nth_smallest_ascii(text):
    chars = sorted([ord(c) for c in text[60:84]])
    return chr(chars[13])