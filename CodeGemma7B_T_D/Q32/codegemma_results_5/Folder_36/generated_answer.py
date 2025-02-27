def insert_after_character(text):
    return ''.join([c + 'H' if c == 'A' else c for c in text])