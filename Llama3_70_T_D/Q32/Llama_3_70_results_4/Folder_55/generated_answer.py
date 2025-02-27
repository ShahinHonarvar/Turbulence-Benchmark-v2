def insert_after_character(s):
    result = ''
    for char in s:
        if char == 'u':
            result += char + 'U'
        else:
            result += char
    return result