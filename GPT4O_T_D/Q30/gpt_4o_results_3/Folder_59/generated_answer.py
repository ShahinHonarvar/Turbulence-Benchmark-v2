def insert_before_character(s):
    return ''.join(('0o' if c == 'o' else c for c in s))