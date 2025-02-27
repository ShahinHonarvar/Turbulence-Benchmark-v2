def insert_after_character(text):
    return ''.join([c + 'y' if c == 'b' else c for c in text])