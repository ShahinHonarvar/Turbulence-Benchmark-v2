def insert_after_character(text):
    return ''.join((c + 'u' if c == 't' else c for c in text))