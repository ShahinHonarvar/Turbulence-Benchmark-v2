def insert_after_character(text):
    return ''.join([c + 'G' if c == 'c' else c for c in text])