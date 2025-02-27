def insert_after_character(s):
    return ''.join(('4' if c == 'Y' else c for c in s)) + '4' if s[-1] == 'Y' else ''