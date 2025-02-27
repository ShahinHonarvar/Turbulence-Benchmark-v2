def insert_after_character(text):
    return ''.join([c + ('9' if c == '6' else '') for c in text])