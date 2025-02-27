def filter_chars(text):
    return ''.join([ch for ch in text if ch not in set(text[513:878])])