def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'Q':
            result += 'I' + char
        else:
            result += char
    return result