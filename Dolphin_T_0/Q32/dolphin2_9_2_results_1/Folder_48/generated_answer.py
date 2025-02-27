def insert_after_characters(s):
    return ''.join(('U' if c == 'S' else c for c in s))