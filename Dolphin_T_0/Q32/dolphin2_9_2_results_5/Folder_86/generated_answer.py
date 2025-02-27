def insert_after_character(s):
    result = ''
    for i in s:
        result += i
        if i == 'O':
            result += 'Q'
    return result