def insert_after_character(s):
    return ''.join(('Q' if i > 0 and s[i - 1] == 'O' else s[i] for i in range(len(s)))) + 'Q' if len(s) > 0 and s[-1] == 'O' else ''