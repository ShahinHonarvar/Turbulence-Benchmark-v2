def filter_chars(text):
    return ''.join([ch for ch in text if not (ch > '!' and ch < '}') and ch not in text[39:87]])