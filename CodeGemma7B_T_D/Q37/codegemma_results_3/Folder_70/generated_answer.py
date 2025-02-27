def filter_chars(text):
    return ''.join([ch for ch in text if ord(ch) < 90 if ord(ch) > 64 if ord(ch) > 538 or ord(ch) < 515])