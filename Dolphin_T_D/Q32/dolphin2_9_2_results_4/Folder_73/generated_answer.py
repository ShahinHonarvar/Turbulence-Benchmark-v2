def insert_after_character(s):
    result = ''
    for i in s:
        result += i
        if i == 'R':
            result += 'V'
    return result