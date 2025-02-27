def insert_after_character(s):
    return ''.join(['O' if i > 0 and s[i - 1] == 'o' else ch for i, ch in enumerate(s)])