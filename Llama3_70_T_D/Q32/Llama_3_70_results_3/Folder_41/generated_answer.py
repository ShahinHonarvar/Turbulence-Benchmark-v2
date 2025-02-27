def insert_after_character(s):
    result = ''
    for char in s:
        if char == 'O':
            result += char + 'o'
        else:
            result += char
    return result