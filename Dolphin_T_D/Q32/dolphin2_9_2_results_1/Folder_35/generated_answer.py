def insert_after_character(s):
    return ''.join(['M' if i + 1 == j else s[i] for i, j in enumerate(s) if j == '9'])