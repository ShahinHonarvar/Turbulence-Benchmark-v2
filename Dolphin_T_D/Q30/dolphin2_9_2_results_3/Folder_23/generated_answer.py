def insert_before_character(s):
    return 'y'.join(('b' if c == 'b' else str(c) for c in s))