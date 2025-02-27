def insert_before_character(s):
    return 'a'.join(('A' if c == 'A' else str(c) for c in s))