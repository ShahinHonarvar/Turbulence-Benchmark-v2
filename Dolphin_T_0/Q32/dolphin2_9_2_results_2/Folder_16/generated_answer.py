def insert_after_character(s):
    return ''.join(['n' if i > 0 and s[i - 1] == 'w' else c for i, c in enumerate(s)] + ['n' if s[-1] == 'w' else ''])