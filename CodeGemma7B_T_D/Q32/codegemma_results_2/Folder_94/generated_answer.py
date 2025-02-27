def insert_after_character(string):
    result = ''
    for char in string:
        if char == ' ':
            result += char + '5'
        else:
            result += char
    return result