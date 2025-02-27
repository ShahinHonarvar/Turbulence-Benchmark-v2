def insert_after_character(s):
    return ''.join(['z' if s[i] == 'N' and i + 1 != len(s) else s[i] for i in range(len(s))])