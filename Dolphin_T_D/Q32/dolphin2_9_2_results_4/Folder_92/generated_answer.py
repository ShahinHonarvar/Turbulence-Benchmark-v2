def insert_after_character(s):
    return 'a'.join(('ab' if c == 'a' else c for c in s))