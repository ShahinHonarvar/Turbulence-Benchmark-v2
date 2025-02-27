def insert_before_character(s):
    result = ''
    for i in s:
        if i == 'N':
            result += 'z' + i
        else:
            result += i
    return result