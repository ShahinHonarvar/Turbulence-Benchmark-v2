def insert_before_character(text):
    return ''.join([c + ('u' if c == 'F' else '') for c in text])