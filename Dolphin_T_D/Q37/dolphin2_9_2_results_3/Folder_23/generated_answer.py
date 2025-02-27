def filter_chars(text):
    for c in range(ord('V'), ord('Y') + 1):
        text = text.replace(chr(c), '')
    return text