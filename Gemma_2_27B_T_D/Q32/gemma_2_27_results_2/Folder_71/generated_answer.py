def insert_after_character(text):
    return ''.join([c + 'S' if c == '2' else c for c in text])