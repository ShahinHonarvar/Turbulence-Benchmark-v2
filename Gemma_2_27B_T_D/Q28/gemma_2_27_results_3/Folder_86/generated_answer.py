def return_nth_smallest_ascii(text):
    chars = sorted([ord(c) for c in text[44:70]])
    if len(chars) >= 15:
        return chr(chars[14])