def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'T':
            result += ' ' + c
        else:
            result += c
    return result