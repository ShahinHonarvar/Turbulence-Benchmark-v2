def insert_after_character(text):
    return ''.join([c + 'e' if c == 'e' else c for c in text])