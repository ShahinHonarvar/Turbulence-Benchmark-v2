def insert_after_character(s):
    return ''.join([c + ('0' if c == 'i' else '') for c in s])