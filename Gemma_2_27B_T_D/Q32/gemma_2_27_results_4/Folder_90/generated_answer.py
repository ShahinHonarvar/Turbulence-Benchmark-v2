def insert_after_character(text):
    return ''.join(['U' + 'F' + c if c == 'U' else c for c in text])