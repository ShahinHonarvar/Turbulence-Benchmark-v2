def filter_chars(text):
    text = ''.join((char for char in text if ord(char) < ord('J') or ord(char) > ord('b') or (not 348 <= text.index(char) <= 852)))
    return text