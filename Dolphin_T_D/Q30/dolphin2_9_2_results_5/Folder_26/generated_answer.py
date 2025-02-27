def insert_before_character(s):
    return 'w'.join(['w' if c == 'r' else c for c in s]) + 'w' if s and s[-1] == 'r' else ''