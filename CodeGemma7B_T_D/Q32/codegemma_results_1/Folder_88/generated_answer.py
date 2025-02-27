def insert_after_character(text):
    return ''.join([ch + 't' if ch == 'a' else ch for ch in text])