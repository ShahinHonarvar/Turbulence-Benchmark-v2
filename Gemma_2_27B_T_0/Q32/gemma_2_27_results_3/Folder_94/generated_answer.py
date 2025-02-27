def insert_after_character(text):
    return ''.join([c + '5' if c == ' ' else c for c in text])