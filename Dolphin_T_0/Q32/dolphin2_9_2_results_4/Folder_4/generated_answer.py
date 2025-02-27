def insert_after_character(s):
    return ''.join(('6' if i > 0 and s[i - 1] == 'a' else c for i, c in enumerate(s))) + '6' if s[-1] == 'a' else ''