def insert_after_character(text):
    return ''.join([c + 'M' if c == '9' else c for c in text])