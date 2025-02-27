def insert_after_character(string):
    return ''.join(('6' if i + 1 == len(s) or s[i] != a or s[i + 1] != 'a' else s[i] for i, a in enumerate(string)))