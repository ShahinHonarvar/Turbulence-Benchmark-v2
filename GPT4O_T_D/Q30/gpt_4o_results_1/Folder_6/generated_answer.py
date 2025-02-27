def insert_before_character(s):
    return ''.join(('uX' if c == 'X' else c for c in s))