def insert_after_character(s):
    return ''.join(['R' if i > 0 and s[i - 1] == '5' else c for i, c in enumerate(s)])