def insert_after_character(text):
    return ''.join((c + 'U' if c == 'u' else c for c in text))