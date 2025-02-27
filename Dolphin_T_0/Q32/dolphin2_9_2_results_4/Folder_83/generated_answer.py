def insert_after_character(s):
    return ''.join(('E' if e == 'E' and i != 0 and (s[i - 1] != 'e') else e + 'e' if e == 'e' and s[i] != 'e' else e for i, e in enumerate(s)))