def insert_before_character(s):
    return 'o'.join(('F' if c == 'F' else '' + s for c in s)).replace('oF', 'F')