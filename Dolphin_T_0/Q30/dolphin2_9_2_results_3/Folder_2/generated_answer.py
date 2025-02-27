def insert_before_character(s):
    return 'Z' if s == '' else ''.join((c if c != 'C' else 'ZC' if i > 0 and s[i - 1] != 'Z' else 'C' for i, c in enumerate(s)))