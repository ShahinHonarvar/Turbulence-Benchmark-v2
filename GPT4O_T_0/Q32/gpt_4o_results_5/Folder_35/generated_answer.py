def insert_after_character(s):
    return ''.join((c + 'M' if c == '9' else c for c in s))