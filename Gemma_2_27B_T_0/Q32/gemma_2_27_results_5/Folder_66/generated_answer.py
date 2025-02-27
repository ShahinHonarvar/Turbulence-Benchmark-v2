def insert_after_character(text):
    return ''.join([c + 'k' if c == 'k' else c for c in text])