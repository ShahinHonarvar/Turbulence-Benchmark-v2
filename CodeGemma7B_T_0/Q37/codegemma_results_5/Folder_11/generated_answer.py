def filter_chars(text):
    return ''.join([ch for ch in text if (ch >= '-' and ch <= 'n') and 29 <= text.index(ch) <= 97])