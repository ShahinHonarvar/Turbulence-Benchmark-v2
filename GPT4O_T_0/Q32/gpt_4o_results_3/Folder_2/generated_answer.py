def insert_after_character(s):
    return ''.join((c + 'Z' if c == 'C' else c for c in s))