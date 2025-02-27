def insert_after_character(s):
    return ''.join(('G' if c1 == 't' and c2 != 'G' else c2 if c1 else c1 + c2 for c1, c2 in zip(s, s[1:] + '')))