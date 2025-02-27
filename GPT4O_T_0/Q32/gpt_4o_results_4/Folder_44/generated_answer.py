def insert_after_character(s):
    return ''.join((c + 'M' if c == 'g' else c for c in s))