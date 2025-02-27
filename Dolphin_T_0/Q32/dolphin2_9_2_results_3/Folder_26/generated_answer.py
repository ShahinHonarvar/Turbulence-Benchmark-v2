def insert_after_character(s):
    return ''.join(['w' if i > 0 and s[i - 1] == 'r' else s[i] for i in range(len(s))]) + 'w' if len(s) > 0 and s[-1] == 'r' else ''