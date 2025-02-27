def insert_after_character(text):
    return ''.join([ch + 'U' if ch == 'u' else ch for ch in text])