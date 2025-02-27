def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'r':
            result += 'w' + c
        else:
            result += c
    return result