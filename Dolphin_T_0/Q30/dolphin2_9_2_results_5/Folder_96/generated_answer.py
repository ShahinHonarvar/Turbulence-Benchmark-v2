def insert_before_character(s):
    return ''.join(['A' if c == 'a' else c for c in s]) + 'A' if s[-1] != 'a' else ''