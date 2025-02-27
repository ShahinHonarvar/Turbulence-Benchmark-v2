def insert_after_character(text):
    return ''.join([c + 'Q' if c == 'm' else c for c in text])