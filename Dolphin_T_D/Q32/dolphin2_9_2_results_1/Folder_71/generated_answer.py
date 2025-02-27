def insert_after_character(s):
    return ''.join(['S' if j == '2' and i + 1 < len(s) and (s[i + 1] != 'S') else s[i] for i, j in enumerate(s)])