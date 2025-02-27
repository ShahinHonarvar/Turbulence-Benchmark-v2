def insert_after_character(s):
    return ''.join([c + 'I' if c == 'i' else c for c in s])