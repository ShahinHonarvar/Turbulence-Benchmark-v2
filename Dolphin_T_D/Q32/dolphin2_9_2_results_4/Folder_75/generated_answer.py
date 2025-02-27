def insert_after_character(s):
    return ''.join(('q' if c == 'U' else c for c in s))