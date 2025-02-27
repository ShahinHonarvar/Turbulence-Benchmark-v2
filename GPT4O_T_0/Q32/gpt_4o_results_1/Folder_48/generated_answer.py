def insert_after_character(s):
    return ''.join((c + 'U' if c == 'S' else c for c in s))