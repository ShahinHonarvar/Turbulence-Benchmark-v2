def insert_before_character(s):
    return 'U'.join(('U' if c == 'U' else s[i] for i, c in enumerate(s)))