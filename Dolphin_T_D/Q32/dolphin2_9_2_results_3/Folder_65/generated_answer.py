def insert_after_character(s):
    return ''.join(('9' if i > 0 and s[i - 1] == '6' else c for i, c in enumerate(s)))