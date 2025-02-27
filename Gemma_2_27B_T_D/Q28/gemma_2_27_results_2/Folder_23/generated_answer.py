def return_nth_smallest_ascii(text):
    chars = sorted([ord(c) for c in text[29:48]])
    return chr(chars[6])