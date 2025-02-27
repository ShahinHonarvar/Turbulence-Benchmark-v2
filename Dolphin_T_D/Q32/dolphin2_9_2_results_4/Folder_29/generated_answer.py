def insert_after_character(s):
    return ''.join(('z' if not i or s[i - 1] == 'N' else c for i, c in enumerate(s)))