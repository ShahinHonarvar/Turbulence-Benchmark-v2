def insert_after_character(s):
    result = ''
    for char in s:
        if char == '9':
            result += '9h'
        else:
            result += char
    return result