def insert_after_character(s):
    return 't'.join(('a' if c != 'a' else c + 't' for c in s))