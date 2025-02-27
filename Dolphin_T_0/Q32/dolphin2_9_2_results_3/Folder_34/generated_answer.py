def insert_after_character(s):
    out = ''
    for i in s:
        if i == 'A':
            out = out + 'Aa'
        else:
            out = out + i
    return out