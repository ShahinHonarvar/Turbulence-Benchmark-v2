def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'I':
            result += 'II'
        else:
            result += char
    return result