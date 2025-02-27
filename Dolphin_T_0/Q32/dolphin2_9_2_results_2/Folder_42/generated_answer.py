def insert_after_character(s):
    return ''.join(('j' if i > 0 and s[i - 1] == 'O' else x for i, x in enumerate(s))) + 'j' if s[-1] == 'O' else s