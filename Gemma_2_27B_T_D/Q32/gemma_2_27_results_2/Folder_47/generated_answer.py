def insert_after_character(text):
    return ''.join([c + 'f' if c == 'E' else c for c in text])