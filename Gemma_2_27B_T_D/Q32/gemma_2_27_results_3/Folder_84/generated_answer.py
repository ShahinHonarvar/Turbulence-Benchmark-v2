def insert_after_character(text):
    return ''.join([c + ('n' if c == 'H' else '') for c in text])