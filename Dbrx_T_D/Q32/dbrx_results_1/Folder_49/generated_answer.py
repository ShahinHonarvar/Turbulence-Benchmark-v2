def insert_after_character(s):
    i_s = ''
    for c in s:
        i_s += c
        if c == 'i':
            i_s += 'i'
    return i_s