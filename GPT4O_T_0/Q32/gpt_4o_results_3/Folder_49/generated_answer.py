def insert_after_character(s):
    return ''.join((c + 'i' if c == 'i' else c for c in s))