def insert_before_character(text_string):
    return ''.join([c + 'N' if c == 'm' else c for c in text_string])