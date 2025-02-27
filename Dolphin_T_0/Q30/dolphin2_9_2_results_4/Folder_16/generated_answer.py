def insert_before_character(s):
    return ''.join(('n' if i + 1 == j else s[j] for i, j in enumerate(s)))