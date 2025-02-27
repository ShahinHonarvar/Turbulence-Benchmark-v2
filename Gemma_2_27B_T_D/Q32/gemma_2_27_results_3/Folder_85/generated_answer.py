def insert_after_character(text):
    return ''.join(['a' + c if c == 'o' else c for c in text])