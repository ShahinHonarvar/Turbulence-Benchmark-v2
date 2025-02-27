def insert_before_character(s):
    return 'H'.join(('A' if c == 'A' else str(c) for c in s))