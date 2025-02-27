def insert_after_character(text):
    return ''.join([ch + 'I' if ch == 'i' else ch for ch in text])