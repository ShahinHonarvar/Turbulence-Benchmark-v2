def insert_before_character(s):
    return ''.join(('ZC' if c == 'C' else c for c in s))