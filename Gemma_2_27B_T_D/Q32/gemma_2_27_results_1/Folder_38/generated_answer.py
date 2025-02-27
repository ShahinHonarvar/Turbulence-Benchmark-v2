def insert_after_character(text):
    return ''.join([c + '6' if c == 'X' else c for c in text])