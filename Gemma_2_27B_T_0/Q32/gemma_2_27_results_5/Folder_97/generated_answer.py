def insert_after_character(text):
    return ''.join([c + 'h' if c == 'o' else c for c in text])