def insert_after_character(s):
    result = ''
    for char in s:
        result += char
        if char == ' ':
            result += '5'
    return result