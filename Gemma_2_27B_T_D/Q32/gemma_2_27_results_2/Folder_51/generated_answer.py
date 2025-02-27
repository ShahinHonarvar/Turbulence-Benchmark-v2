def insert_after_character(text):
    return ''.join(['O' + c if c == 'o' else c for c in text])