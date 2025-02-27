def insert_after_character(text):
    return ''.join([ch + 'e' if ch == 'e' else ch for ch in text])