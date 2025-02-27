def insert_after_character(s):
    return ''.join(['h' if i + 1 == j else s[j] for i, j in enumerate(s)])