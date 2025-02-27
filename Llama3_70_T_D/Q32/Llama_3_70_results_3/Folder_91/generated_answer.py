def insert_after_character(s):
    result = ''
    for c in s:
        result += c
        if c == 'a':
            result += '0'
    return result