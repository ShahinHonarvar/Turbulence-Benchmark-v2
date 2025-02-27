def insert_after_character(s):
    return ''.join(('6' if i == len(s) - 1 and s[i] == 'X' else s[i] for i in range(len(s)) if s[i] == 'X'))