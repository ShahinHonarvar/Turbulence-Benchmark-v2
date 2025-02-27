def insert_after_character(s):
    return ''.join((c + '6' if c == 'X' else c for c in s))