def insert_after_character(s):
    return ''.join((c + 'R' if c == '5' else c for c in s))