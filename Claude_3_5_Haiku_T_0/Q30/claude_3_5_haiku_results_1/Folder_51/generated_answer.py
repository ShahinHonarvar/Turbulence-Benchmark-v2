def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'o':
            result += 'O' + char
        else:
            result += char
    return result