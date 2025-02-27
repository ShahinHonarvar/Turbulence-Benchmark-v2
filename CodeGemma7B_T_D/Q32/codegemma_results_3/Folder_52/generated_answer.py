def insert_after_character(text):
    return ''.join((c + ('V' if c == 'T' else '') for c in text))