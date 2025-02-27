def insert_before_character(s):
    result = ''
    for c in s:
        if c == 't':
            result += 'G' + c
        else:
            result += c
    return result