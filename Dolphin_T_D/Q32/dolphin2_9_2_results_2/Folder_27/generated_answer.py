def insert_after_character(s):
    return ''.join(('j' if c == 'N' and i < len(s) - 1 else s[i] for i, c in enumerate(s)))