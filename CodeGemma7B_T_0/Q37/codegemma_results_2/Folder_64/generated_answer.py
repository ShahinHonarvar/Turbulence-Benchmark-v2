def filter_chars(text):
    return ''.join([ch for ch in text if ch not in text[1:8] or not (ch >= 'L' and ch <= 'a')])