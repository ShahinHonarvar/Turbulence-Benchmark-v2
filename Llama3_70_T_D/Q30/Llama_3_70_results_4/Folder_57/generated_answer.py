def insert_before_character(s):
    result = ''
    for i in s:
        if i == 's':
            result += 'w'
        result += i
    return result