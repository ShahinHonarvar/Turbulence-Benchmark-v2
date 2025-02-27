def insert_after_character(s):
    return ''.join((c + 'Q' if c == 'm' else c for c in s))