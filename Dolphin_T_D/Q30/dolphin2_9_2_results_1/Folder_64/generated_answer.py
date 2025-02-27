def insert_before_character(s):
    return 'u'.join(('u' if c == 'u' else str(c) for c in s))