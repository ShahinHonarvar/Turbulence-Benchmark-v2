def insert_after_character(s):
    return '0'.join(('0' if c == 'o' else str(c) for c in s))