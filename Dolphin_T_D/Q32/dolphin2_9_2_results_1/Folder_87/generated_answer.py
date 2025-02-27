def insert_after_character(s):
    return ''.join(['N' if i and s[i - 1] == 'm' else s[i] for i in range(len(s))])