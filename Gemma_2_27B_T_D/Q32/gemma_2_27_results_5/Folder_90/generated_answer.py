def insert_after_character(s):
    return ''.join(['UF' if c == 'U' else c for c in s])