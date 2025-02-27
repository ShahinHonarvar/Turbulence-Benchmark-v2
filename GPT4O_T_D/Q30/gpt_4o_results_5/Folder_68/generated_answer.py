def insert_before_character(s):
    return ''.join(('0i' if c == 'i' else c for c in s))