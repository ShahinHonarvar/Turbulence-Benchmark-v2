def insert_after_character(s):
    return ''.join(('t' if c == 'a' else c for c in s)).replace('at', 'a')