def insert_before_character(s):
    return ''.join(('mF' if c == 'F' else c for c in s))