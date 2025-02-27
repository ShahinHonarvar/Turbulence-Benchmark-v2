def insert_after_character(text):
    return ''.join([c + 'N' if c == 'x' else c for c in text])