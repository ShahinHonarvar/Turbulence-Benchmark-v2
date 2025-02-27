def insert_before_character(text):
    return ''.join((ch + '0' if ch == 'e' else ch for ch in text))