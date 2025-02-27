def insert_after_character(s):
    return ''.join(('F' if i > 0 and s[i - 1] == 'U' else c for i, c in enumerate(s)))