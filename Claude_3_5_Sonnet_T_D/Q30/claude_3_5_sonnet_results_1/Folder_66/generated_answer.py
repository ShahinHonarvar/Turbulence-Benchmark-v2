def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'k':
            result += 'kk'
        else:
            result += char
    return result