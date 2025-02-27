def insert_after_character(text):
    return ''.join([c + 'I' if c == 'Q' else c for c in text])