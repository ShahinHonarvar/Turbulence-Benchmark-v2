def insert_after_character(text):
    return ''.join(['H' + c if c == '0' else c for c in text])