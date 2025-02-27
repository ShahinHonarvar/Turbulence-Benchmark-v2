def insert_before_character(s):
    new_s = ''
    for c in s:
        new_s += 'o' if c == 'o' else '' + c
    return new_s