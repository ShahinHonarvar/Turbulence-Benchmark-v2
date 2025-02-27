def insert_after_character(s):
    return ''.join((c + 'j' if c == 'N' else c for c in s))