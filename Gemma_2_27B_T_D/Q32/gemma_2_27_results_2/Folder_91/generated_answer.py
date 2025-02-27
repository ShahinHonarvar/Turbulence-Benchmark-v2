def insert_after_character(text):
    return ''.join(['a' + '0' if c == 'a' else c for c in text])