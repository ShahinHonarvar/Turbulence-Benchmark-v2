def insert_after_character(s):
    return ''.join(['d' if i > 0 and s[i - 1] == 'O' else s[i] for i in range(len(s))])