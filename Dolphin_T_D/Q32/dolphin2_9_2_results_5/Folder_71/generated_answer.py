def insert_after_character(s):
    return ''.join(('S' if i > 0 and s[i - 1] == '2' else c for i, c in enumerate(s)))