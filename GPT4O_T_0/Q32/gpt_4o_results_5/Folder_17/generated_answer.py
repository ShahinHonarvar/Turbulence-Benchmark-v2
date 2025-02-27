def insert_after_character(s):
    return ''.join((c + 'I' if c == 'Q' else c for c in s))