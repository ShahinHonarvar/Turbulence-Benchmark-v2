def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'b':
            result += 'y' + char
        else:
            result += char
    return result