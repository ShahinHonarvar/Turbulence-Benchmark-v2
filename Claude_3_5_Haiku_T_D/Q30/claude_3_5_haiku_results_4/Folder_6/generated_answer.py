def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'X':
            result += 'u' + char
        else:
            result += char
    return result