def insert_after_character(s):
    return ''.join((c + 'S' if c == '2' else c for c in s))