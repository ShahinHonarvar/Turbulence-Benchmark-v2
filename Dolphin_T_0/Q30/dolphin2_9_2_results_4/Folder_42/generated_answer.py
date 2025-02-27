def insert_before_character(s):
    return ''.join(('j' if c == 'O' and s[i - 1] != 'j' else c for i, c in enumerate(s)))