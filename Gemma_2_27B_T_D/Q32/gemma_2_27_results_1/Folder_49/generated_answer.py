def insert_after_character(text):
    return ''.join([c + 'i' if c == 'i' else c for c in text])