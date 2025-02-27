def insert_after_character(s):
    return ''.join(('e' if c == 'e' and i > 0 and (s[i - 1] == 'e') else c for i, c in enumerate(s)))