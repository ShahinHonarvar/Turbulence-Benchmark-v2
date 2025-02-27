def insert_before_character(s):
    return ''.join(['f' if c == 'E' else c for c in s]) + 'f' if s[-1] == 'E' else ''