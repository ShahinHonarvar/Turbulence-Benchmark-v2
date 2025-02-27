def insert_after_character(s):
    o = ''
    for c in s:
        o += c
        if c == '0':
            o += ' '
    return o