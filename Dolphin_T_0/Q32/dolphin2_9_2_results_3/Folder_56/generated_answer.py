def insert_after_character(s):
    return ''.join(['I' if c == 'I' else c + 'i' if c == 'i' else c for c in s])