def insert_before_character(s):
    return ' '.join(('T' if c == 'T' else str(c) for c in s)).replace('T', ' T')