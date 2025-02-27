def insert_after_character(s):
    return ''.join(('s' if i == 0 or s[i - 1] == 'H' else c for i, c in enumerate(s)))