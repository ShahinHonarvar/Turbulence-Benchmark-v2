def insert_after_character(s):
    return ''.join((c + 'V' if c == 'T' else c for c in s))