def insert_after_character(s):
    return ''.join(('R' if i + 1 == j else s[j] for i, j in enumerate(s.replace('5', '5R'))))