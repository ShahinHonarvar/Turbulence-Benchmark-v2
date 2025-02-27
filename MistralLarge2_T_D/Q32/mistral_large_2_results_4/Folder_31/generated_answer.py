def insert_after_character(s):
    return ''.join((c + 'N' if c == 'B' else c for c in s))