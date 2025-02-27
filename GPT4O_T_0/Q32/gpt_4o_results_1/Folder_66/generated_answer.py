def insert_after_character(s):
    return ''.join((c + 'k' if c == 'k' else c for c in s))