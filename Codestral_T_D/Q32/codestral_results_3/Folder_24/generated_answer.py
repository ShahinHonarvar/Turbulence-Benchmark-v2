def insert_after_character(string):
    result = ''
    for char in string:
        if char == '0':
            result += char + '4'
        else:
            result += char
    return result