def insert_after_character(s):
    return ''.join(['0' if i and s[i - 1] == 'a' else s[i] for i, c in enumerate(s)])