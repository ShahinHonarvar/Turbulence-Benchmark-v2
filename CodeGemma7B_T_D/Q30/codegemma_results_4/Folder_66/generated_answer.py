def insert_before_character(text):
    return ''.join((c if c != 'k' else 'k' + c for c in text))