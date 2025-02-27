def filter_chars(text):
    return ''.join((ch for ch in text if ord(ch) >= 75 and ord(ch) <= 97))