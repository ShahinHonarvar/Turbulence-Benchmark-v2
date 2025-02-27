def insert_after_character(s):
    return ''.join(('j' if c == 'O' and i != 0 and (s[i - 1] == 'O') else c for i, c in enumerate(s)))