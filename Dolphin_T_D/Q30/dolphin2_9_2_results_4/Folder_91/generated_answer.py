def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'a':
            result = result + '0'
        result = result + c
    return result