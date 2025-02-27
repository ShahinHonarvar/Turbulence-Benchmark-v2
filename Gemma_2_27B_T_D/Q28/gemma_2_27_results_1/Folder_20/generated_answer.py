def return_nth_smallest_ascii(text):
    chars = sorted([ord(c) for c in text[25:65]])
    return chr(chars[5])