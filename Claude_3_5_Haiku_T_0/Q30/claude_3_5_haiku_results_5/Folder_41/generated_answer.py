def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'O':
            result += 'o' + char
        else:
            result += char
    return result