def insert_after_character(s):
    return ''.join(('4' if i + 1 == j else s[j] for i, j in enumerate(s)))