def insert_after_character(s):
    return ''.join(('Uu' if c == 'U' else c for c in s))