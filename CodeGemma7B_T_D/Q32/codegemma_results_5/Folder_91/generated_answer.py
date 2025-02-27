def insert_after_character(text):
    return ''.join((ch + '0' if ch == 'a' else ch for ch in text))