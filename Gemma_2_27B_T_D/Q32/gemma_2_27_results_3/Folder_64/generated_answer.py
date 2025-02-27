def insert_after_character(text):
    return ''.join([c if c != 'u' else 'uu' for c in text])