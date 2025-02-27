def insert_after_character(s):
    return ''.join(('u' if i > 0 and s[i - 1] == 't' else c for i, c in enumerate(s)))