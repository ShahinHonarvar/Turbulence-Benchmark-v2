def insert_before_character(s):
    return ''.join(('S' if c == '2' else s[i] for i, c in enumerate(s)))