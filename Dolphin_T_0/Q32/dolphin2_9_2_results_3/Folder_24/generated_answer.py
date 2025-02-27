def insert_after_character(s):
    return ''.join(['4' if s[i] == '0' and i < len(s) - 1 else s[i] for i in range(len(s))])