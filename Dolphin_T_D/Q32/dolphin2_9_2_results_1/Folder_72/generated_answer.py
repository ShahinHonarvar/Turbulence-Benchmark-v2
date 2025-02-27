def insert_after_character(s):
    return ''.join(['d' if i + 1 == j else s[j] for i, j in enumerate(s) if s[i:i + 2] == 'Od'])