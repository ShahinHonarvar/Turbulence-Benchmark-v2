def insert_before_character(str):
    return ''.join([c + ('u' if c == 'u' else '') for c in str])