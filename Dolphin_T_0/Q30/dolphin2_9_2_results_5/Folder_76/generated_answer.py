def insert_before_character(s):
    result = ''
    for i in s:
        if i == 'F':
            result += 'm'
        result += i
    return result