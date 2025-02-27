def insert_after_character(s):
    return ' '.join(('X' if c == ' ' else str(c) for c in s))