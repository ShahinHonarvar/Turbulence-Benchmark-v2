def insert_after_character(s):
    return 'u'.join([c + ('u' if c == 'u' else '') for c in s])