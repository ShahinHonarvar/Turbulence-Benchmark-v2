def insert_after_character(text):
    return ''.join([c + 'o' if c == 'o' else c for c in text])