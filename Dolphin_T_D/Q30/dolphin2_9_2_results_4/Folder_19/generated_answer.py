def insert_before_character(s):
    result = ''
    for c in s:
        if c == '5':
            result += 'h' + c
        else:
            result += c
    return result