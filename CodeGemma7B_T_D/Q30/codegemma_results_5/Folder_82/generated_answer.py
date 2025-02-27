def insert_before_character(text):
    return ''.join((c + 'I' if c == 'I' else c for c in text))