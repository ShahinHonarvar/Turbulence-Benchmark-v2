def insert_after_character(s):
    return ''.join(('d' if c == 'O' and i < len(s) - 1 else s[i] for i, c in enumerate(s))) + ('d' if s[-1] == 'O' else '')