def insert_after_character(s):
    return ''.join(['0' if s[i] == 'a' and i != 0 else s[i] for i in range(len(s))])