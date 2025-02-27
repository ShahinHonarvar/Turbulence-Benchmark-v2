def insert_before_character(s):
    result = ''
    for char in s:
        if char == ' ':
            result += '5'
        result += char
    return result