def insert_after_character(text):
    return ''.join([c + 'j' if c == 'O' else c for c in text])