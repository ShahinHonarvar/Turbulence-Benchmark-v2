def insert_after_character(s):
    return ''.join([c + ('l' if c == 'K' else '') for c in s])