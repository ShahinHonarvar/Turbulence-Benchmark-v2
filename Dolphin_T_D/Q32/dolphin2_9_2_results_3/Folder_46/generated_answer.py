def insert_after_character(s):
    return ''.join(['W' if i > 0 and s[i - 1] == '6' else s[i] for i, c in enumerate(s)]) + 'W' if s[-1] == '6' else ''