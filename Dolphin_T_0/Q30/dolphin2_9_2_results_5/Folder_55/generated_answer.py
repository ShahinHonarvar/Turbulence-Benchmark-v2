def insert_before_character(s):
    return 'U'.join(('u' if c == 'u' else str(c) for c in s))