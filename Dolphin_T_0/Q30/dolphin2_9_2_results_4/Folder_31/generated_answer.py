def insert_before_character(s):
    return 'N'.join(('B' if c == 'B' else '' if c == 'N' else c for c in s))