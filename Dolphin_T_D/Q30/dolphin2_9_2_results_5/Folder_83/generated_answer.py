def insert_before_character(s):
    result = ''
    for i in s:
        if i == 'E':
            result += 'e' + i
        else:
            result += i
    return result