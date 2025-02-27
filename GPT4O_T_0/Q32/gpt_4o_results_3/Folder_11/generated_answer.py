def insert_after_character(s):
    return ''.join((c + 't' if c == 'g' else c for c in s))