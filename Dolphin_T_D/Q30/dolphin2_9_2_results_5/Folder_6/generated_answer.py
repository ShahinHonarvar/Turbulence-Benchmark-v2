def insert_before_character(s):
    result = ''
    for i in s:
        if i == 'X':
            result += 'u' + i
        else:
            result += i
    return result