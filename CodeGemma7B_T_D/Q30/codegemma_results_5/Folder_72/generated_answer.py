def insert_before_character(text):
    return ''.join((ch + 'd' if ch == 'O' else ch for ch in text))