def insert_after_character(text):
    return ''.join([c + 'z' if c == 'N' else c for c in text])