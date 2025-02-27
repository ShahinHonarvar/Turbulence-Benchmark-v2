def insert_after_character(s):
    return ''.join(('1' if i > 0 and s[i - 1] == 'r' else s[i] for i in range(len(s)))) + '1' if len(s) > 0 and s[-1] == 'r' else ''