def insert_after_character(text):
    return ''.join([c + 'a' if c == 'a' else c for c in text])