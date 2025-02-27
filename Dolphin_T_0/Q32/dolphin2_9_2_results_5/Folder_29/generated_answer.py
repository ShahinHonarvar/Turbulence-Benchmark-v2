def insert_after_character(s):
    return ''.join(['z' if i + 1 < len(s) and s[i + 1] == 'N' else s[i] for i in range(len(s))])