def insert_after_character(s):
    return ''.join([c for i, c in enumerate(s) if i == 0 or (s[i - 1] != 'k' and c != 'k') or (s[i - 1] == 'k' and c == 'k')])