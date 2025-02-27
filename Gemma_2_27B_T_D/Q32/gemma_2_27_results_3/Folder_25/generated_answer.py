def insert_after_character(text):
    return ''.join([c + 'W' if c == 'e' else c for c in text])