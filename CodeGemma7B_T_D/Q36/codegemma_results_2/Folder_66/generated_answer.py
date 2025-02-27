def filter_chars(text):
    return ''.join([ch for ch in text if ord(ch) not in range(ord('!') + 1, ord('}') + 1)])