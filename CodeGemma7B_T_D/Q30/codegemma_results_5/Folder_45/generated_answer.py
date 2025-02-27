def insert_before_character(text):
    return ''.join((c + 'O' if c == 'O' else c for c in text))