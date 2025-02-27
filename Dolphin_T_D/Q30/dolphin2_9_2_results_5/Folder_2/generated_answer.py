def insert_before_character(s):
    return 'Z'.join(('C' if c == 'C' else '' + c for c in s)) + 'C' * (s[-1] == 'C')