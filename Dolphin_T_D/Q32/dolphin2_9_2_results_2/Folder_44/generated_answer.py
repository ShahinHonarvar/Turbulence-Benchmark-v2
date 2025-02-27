def insert_after_character(s):
    return ''.join(['M' if i > 0 and s[i - 1] == 'g' else c for i, c in enumerate(s)] + ['M' if s[-1] == 'g' else ''])