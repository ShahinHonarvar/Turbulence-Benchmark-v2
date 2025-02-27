def insert_after_character(text):
    return ''.join([c + 's' if c == 'H' else c for c in text])