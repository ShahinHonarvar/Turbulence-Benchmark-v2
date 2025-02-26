def insert_after_character(s):
    result = ''
    for char in s:
        if char == 'w':
            result += 'wn'
        else:
            result += char
    return result