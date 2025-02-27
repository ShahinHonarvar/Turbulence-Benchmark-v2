def insert_before_character(s):
    result = ''
    for i, c in enumerate(s):
        if c == 'E':
            result += 'T' + c
        else:
            result += c
    return result