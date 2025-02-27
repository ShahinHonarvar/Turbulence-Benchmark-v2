def insert_after_character(s):
    return ''.join(['H' if i > 0 and s[i - 1] == 'C' else c for i, c in enumerate(s)]) + s[-1] if s[-1] != 'C' else s + 'H'