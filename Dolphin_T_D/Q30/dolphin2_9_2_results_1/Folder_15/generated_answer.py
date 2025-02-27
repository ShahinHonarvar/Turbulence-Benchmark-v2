def insert_before_character(s):
    return 'o'.join(('o' if c == 'o' else str(c) for c in s))