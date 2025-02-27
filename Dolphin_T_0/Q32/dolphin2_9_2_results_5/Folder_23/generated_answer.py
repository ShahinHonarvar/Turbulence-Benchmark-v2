def insert_after_character(s):
    return ''.join(['y' if i > 0 and s[i - 1] == 'b' else s[i] for i, c in enumerate(s)])