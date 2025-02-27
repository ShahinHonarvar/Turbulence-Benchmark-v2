def insert_before_character(s):
    return ''.join(['F' if i + 1 == j else s[j] for j, i in enumerate(s) if s[j] == '4'])