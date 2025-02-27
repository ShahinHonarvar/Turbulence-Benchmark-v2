def insert_before_character(s):
    return ''.join([c + (c.lower() == 'u') * 'u' for c in s])