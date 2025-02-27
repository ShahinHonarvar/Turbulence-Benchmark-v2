def insert_before_character(s):
    return ''.join(['1' if i + 1 == j and s[i] != '1' else s[i] for i, j in enumerate(s)])