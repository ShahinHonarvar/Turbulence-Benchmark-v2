def insert_before_character(str):
    return ''.join((c + ('o' if c.lower() == 'o' else '') for c in str))