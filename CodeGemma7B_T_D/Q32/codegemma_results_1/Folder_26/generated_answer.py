def insert_after_character(s):
    result = ''
    for char in s:
        if char == 'r':
            result += char + 'w'
        else:
            result += char
    return result