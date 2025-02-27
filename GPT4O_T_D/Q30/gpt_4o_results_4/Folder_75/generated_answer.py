def insert_before_character(s):
    return ''.join(('qU' if c == 'U' else c for c in s))