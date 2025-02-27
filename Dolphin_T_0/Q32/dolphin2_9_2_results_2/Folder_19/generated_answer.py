def insert_after_character(s):
    return ''.join(['h' if i == 5 and j == 0 else s[i] for i, j in enumerate(s)])