def insert_after_character(s):
    return ''.join(('i' if c == 'I' and i < len(s) and (s[i + 1] != 'i') else c for i, c in enumerate(s)))