def insert_after_character(s):
    return ''.join(('R' if c == '5' and i < len(s) - 1 else s[i] for i, c in enumerate(s)))