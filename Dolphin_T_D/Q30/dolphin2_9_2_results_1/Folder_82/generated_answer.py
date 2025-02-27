def insert_before_character(s):
    ret = ''
    for c in s:
        if c == 'I':
            ret += 'I' + c
        else:
            ret += c
    return ret