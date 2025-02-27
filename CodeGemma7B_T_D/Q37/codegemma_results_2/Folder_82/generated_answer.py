def filter_chars(text):
    return ''.join([ch for ch in text if ord(ch) < 80 or ord(ch) > 120])