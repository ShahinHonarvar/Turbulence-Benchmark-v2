def insert_after_character(s):
    return ''.join(['A' + s[i] if i > 0 and s[i - 1] == 'A' else s[i] for i in range(len(s))])