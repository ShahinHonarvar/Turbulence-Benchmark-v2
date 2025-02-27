def insert_before_character(s):
    return ''.join(['6' if i + 1 == j else s[j] for j, i in enumerate(s) if s[i] == 'X' or s[i] == '6'])