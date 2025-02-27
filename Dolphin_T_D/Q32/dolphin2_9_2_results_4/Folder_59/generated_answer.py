def insert_after_character(s):
    return ''.join(['0' if i != j and s[j] == 'o' else s[j] for i, j in enumerate(s)])