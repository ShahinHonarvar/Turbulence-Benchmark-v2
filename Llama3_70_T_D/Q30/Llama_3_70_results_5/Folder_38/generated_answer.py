def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'X':
            result += '6'
        result += c
    return result