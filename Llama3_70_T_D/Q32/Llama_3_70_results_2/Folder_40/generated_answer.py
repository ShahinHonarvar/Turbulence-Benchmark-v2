def insert_after_character(s):
    return ''.join(('ee' if c == 'e' else c for c in s))