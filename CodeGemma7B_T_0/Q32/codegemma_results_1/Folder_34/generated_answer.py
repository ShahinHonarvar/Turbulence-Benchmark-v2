def insert_after_character(text):
    return ''.join([ch + 'a' if ch == 'A' else ch for ch in text])