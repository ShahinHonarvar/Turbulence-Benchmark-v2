def insert_before_character(s):
    return ''.join(['j' if i + 1 < len(s) and s[i + 1] == 'N' else c for i, c in enumerate(s)]) + ('j' if s[-1] == 'N' else '')