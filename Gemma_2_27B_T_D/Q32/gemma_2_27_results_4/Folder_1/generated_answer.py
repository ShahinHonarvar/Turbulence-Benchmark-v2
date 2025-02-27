def insert_after_character(text):
    return ''.join([c + 'T' if c == 'U' else c for c in text])