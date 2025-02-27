def insert_after_character(text):
    return ''.join([c + ('W' if c == '6' else '') for c in text])