def insert_after_character(s):
    return ''.join(('O' if c == 'o' and i > 0 and (s[i - 1] != 'o') else c for i, c in enumerate(s)))