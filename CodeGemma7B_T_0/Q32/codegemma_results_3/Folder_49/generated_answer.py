def insert_after_character(text):
    return ''.join([ch + 'i' if ch == 'i' else ch for ch in text])