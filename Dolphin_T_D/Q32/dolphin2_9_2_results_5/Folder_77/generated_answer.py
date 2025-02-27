def insert_after_character(s):
    return ''.join(['h' if i > 0 and s[i - 1] == '9' else x for i, x in enumerate(s)])