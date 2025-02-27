def insert_after_character(text):
    return ''.join([c + 'n' if c == 'w' else c for c in text])