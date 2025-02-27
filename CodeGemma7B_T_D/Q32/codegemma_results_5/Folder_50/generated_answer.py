def insert_after_character(s):
    return ''.join([c + ('u' if c == 't' else '') for c in s])