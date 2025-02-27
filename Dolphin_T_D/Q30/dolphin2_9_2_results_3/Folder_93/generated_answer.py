def insert_before_character(s):
    return ''.join(['4' if i + 1 == j else s[j - 1] for j, i in enumerate(s) if s[i] == 'Y'])