def insert_after_character(s):
    return ''.join((c + 'm' if c == 'F' else c for c in s))