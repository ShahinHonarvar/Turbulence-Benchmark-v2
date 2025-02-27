def insert_before_character(s):
    return ''.join([('A' if i + 1 < len(s) and s[i + 1] == 'A' else '') + s[i] for i in range(len(s))])