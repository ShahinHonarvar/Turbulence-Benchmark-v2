def insert_before_character(s):
    result = ''
    for char in s:
        if char == 't':
            result += 'u' + char
        else:
            result += char
    return result