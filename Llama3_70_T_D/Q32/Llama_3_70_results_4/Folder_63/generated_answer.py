def insert_after_character(s):
    result = ''
    for char in s:
        if char == '5':
            result += char + 'R'
        else:
            result += char
    return result