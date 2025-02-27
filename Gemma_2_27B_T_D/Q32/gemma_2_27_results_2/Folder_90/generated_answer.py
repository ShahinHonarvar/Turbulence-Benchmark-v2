def insert_after_character(text):
    return ''.join(['F' + c if c == 'U' else c for c in text])