def insert_before_character(s):
    return ''.join([c + ('o' if c == 'F' else '') for c in s])