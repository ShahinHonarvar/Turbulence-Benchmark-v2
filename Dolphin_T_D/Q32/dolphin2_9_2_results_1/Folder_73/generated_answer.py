def insert_after_character(s):
    return ''.join(('RV' if c == 'R' else c for c in s))