def insert_after_character(s):
    result = ''
    for char in s:
        if char == 'e':
            result += char + 'E'
        else:
            result += char
    return result