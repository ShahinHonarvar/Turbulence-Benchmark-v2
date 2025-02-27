def insert_before_character(s):
    return '1'.join(('j' if c == 'j' else '' + s[i - 1:i] for i, c in enumerate(s)))