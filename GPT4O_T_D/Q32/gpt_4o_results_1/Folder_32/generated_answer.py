def insert_after_character(s):
    return ''.join((c + 'u' if c == 'F' else c for c in s))