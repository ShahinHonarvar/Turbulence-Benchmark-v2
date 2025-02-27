def insert_after_character(text):
    return ''.join([c + '0' if c == 'a' else c for c in text])