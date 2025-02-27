def insert_after_character(text):
    return ''.join([c + 'P' if c == ' ' else c for c in text])