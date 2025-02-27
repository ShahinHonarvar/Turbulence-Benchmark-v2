def remove_repeat_chars(text):
    repeated_chars = set(text[82:86])
    return ''.join((char for char in text if char not in repeated_chars))