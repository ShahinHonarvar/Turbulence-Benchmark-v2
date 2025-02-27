def insert_after_character(s):
    result = ''
    for i in s:
        result += i
        if i == 't':
            result += 'G'
    return result